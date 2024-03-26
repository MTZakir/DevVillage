import threading
from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_recaptcha import ReCaptcha
from firebase_admin import db, auth
from auth_forms import OTPForm, PasswordResetEmailForm, PasswordResetForm
from auth_routes import generate_otp_for_email_verification


verify_blueprint = Blueprint(
    "verify", __name__, static_folder="static", template_folder="templates"
)

# Initialize recaptcha
recaptcha = ReCaptcha()

# ---------- VERIFY ACCOUNT ----------
@verify_blueprint.route('/verify', methods=['GET', 'POST'])
def verify():
    # The user might be redirected from either register page or password reset page.
    source = request.args.get('source')

    if not session.get('verify'):
        return redirect(url_for('home'))
    
    form = OTPForm()

    user_id = session.get('verify')

    otp_ref = db.reference('/otp').child(user_id).get()

    # Call delete_otp with delay using threading
    threading.Timer(30, delete_otp, args=(user_id,)).start()

    if form.validate_on_submit() and recaptcha.verify():
        if form.otp.data == otp_ref:

            if source == "register":
                # Updating organization's account with organization name
                auth.update_user(
                    user_id,
                    email_verified = True
                )
                
                session.pop('verify', None)

            elif source == 'resetpass':
                session.pop('mode', None)
                session['mode'] = "show_password"
                return redirect(url_for('verify.reset_pass', mode='show_password'))

            # Redirecting user to corresponding account login page
            if not db.reference("/org_accounts").child(user_id).get():
                return redirect(url_for('auth.user_login'))
            else:
                return redirect(url_for('auth.org_login'))
        
        else:
            print("OTP not correct")
    else:
        print("Invalid form submission.")


    return render_template('temp/verify.html', form = form)

# ---------- RESET PASSWORD ----------
# Page for implementing password reset along with verifying email before resetting password
@verify_blueprint.route('/resetpass', methods=['GET', 'POST'])
def reset_pass():
    # if user is redirected here from login page then the mode is None, then it shows Email text field for the user to verify that the account is theirs
    # If user is redirected here from verify page then the mode is 'show_passowrd' then the display changes to password and confirm password fields


    # MAJOR ISSUE: User is able to go to password change page without needing verification
    # SOLUTION: Either seperate email and password pages, OR use some shitty solution


    mode = request.args.get('mode')

    form = PasswordResetEmailForm()

    display = False
    print(mode)
    if mode == 'show_password':
        form = PasswordResetForm()
        display = True

    user_id = session.get('verify')

    print(user_id)

    if form.validate_on_submit():
        session.pop('verify', None)
        print(mode)
        if mode == 'show_password':    
            password = form.password.data
            confpass = form.confirm_pass.data

            if password == confpass:
                # Update password
                auth.update_user(user_id, password=password)

                # Redirecting user to corresponding account login page
                if not db.reference("/org_accounts").child(user_id).get():
                    return redirect(url_for('auth.user_login'))
                else:
                    return redirect(url_for('auth.org_login'))
        else:
            session['verify'] = auth.get_user_by_email(form.email.data).uid
            generate_otp_for_email_verification(form.email.data)
            return redirect(url_for('verify.verify', source = 'resetpass'))
        

    return render_template('temp/reset_pass.html', form=form, show_password_fields=display)

def delete_otp(user_id):
    db.reference('/otp').child(user_id).delete()

    user = auth.get_user(user_id)

    if not user.email_verified:
        auth.delete_user(user_id)
        if not db.reference("/org_accounts").child(user.uid).get():
            db.reference("/user_accounts").child(user.display_name).delete()
        else:
            db.reference("/org_accounts").child(user.uid).delete()