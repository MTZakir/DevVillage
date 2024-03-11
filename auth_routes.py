import re
import threading
import time
from email_validator import validate_email
from flask import Blueprint, render_template, request, session, redirect, url_for
from firebase_admin import db, auth
from firebase_admin._auth_utils import EmailAlreadyExistsError, PhoneNumberAlreadyExistsError, UserNotFoundError
from flask_recaptcha import ReCaptcha
from auth_forms import OTPForm, OrganizationLoginForm, OrganizationRegistrationForm, PasswordResetEmailForm, UserLoginForm, UserRegistrationForm, PasswordResetForm
import pyrebase, smtplib, string, random

# Blueprint initialization
auth_blueprint = Blueprint(
    "auth", __name__, static_folder="static", template_folder="templates"
)


# Configuration for filipino firebase
pyrebase_config = {
    "apiKey": "AIzaSyDPEdHrwpZOvi0d1d1fUx1WOrX1RJ3TYHc",
    "authDomain": "codebase-93435.firebaseapp.com",
    "databaseURL": "https://codebase-93435-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "codebase-93435",
    "storageBucket": "codebase-93435.appspot.com",
    "messagingSenderId": "580884701092",
    "appId": "1:580884701092:web:b4f7be265ee7ad59b9ab31",
    "measurementId": "G-JRZ98QNRSL"
}

# Initializing pyrebase (For Login)
firebase = pyrebase.initialize_app(pyrebase_config)
pyre_auth = firebase.auth()

# Initialize recaptcha
recaptcha = ReCaptcha()

# ---------- TESTING -----------------------------

@auth_blueprint.route('/check')
def check():
    print('Is user', auth.get_user(session.get('user_id')).display_name ,'verified:', auth.get_user(session.get('user_id')).email_verified)
    session_remove_if_not_verified()
    print(session.get('user_id'))
    return render_template('home.html')

@auth_blueprint.route('/logout')
def logout():
    session_remove_if_not_verified()
    session.pop('user_id', None)
    print("User logged out")
    return render_template('home.html')

# ------------------------------------------------


# Function to authorize users with firebase
def try_login(user_email, user_pass):
    try:
        pyre_auth.sign_in_with_email_and_password(user_email, user_pass)

        user_id = auth.get_user_by_email(user_email).uid

        session['user_id'] = user_id

        print("SUCCESSFULLY LOGGED IN!")
    except:
        print("Incorrect username/email or password.")


# ---------- USER LOGIN ----------
@auth_blueprint.route('/user_login', methods=['GET', 'POST'])
def user_login():
    session_remove_if_not_verified()
    form = UserLoginForm()

    # If no users are logged in
    if session.get("user_id") == None:
        user_ref = db.reference("/user_accounts")
        org_ref = db.reference("/org_accounts")
        
        if form.validate_on_submit():
            # If input is email
            try:
                validate_email(form.username_or_email.data)

                # Get username linked to email if it exists in the database
                username = auth.get_user_by_email(form.username_or_email.data).display_name

                # If given username doesnt exist in user list and organization list
                if user_ref.child(username).get() == None and org_ref.child(username).get() == None:
                    print("An account with that email doesn't exist. Try logging in as an organization instead?")

                # If given username exists in user list (induvidual account), then allow login
                if user_ref.child(username).get() != None:
                    if auth.get_user_by_email(form.username_or_email.data).email_verified:
                        try_login(form.username_or_email.data, form.password.data)
                    else:
                        session['verify'] = auth.get_user_by_email(form.username_or_email.data).uid
                        return redirect(url_for('auth.verify'))

                # If given username exists in organization list (organization account), then prevent login from induvidual page
                if org_ref.child(username).get() != None:
                    print("An account with that email doesn't exist. Try logging in as an organization instead?")

            # If input is username
            except Exception as e:
                
                if user_ref.get() != None:
                    # Get email linked to specified username if it exists
                    try:
                        user_email = user_ref.child(form.username_or_email.data).child("Email").get()

                        if user_ref.child(form.username_or_email.data).get() != None:
                            if auth.get_user_by_email(user_email).email_verified:
                                try_login(user_email, form.password.data)
                            else:
                                session['verify'] = auth.get_user_by_email(user_email).uid
                                return redirect(url_for('auth.verify'))

                    except Exception as e:
                        print("An account with that email doesn't exist. Try logging in as an organization instead?", e)
                else:
                    print("User list is empty.")

        else:
            print("Login form incorrect: ", form.errors)
        
    # If a user is already logged in
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('home'))

    return render_template("temp/user_login.html", form = form)


# ---------- USER REGISTER ----------
@auth_blueprint.route('/user_register', methods=['GET', 'POST'])
def user_register():
    session_remove_if_not_verified()
    form = UserRegistrationForm()
    # If no accounts are logged in
    if session.get("user_id") == None:
        if form.validate_on_submit() and recaptcha.verify():
            user_ref = db.reference("/user_accounts")

            # If user_accounts list is not empty AND username already exists in user_accounts list
            if user_ref.get() != None and form.username.data in user_ref.get():
                print("Username already exists")
            
            # Else create user
            else:
                try:
                    # Creating new account with email and password
                    new_user = auth.create_user(
                        email = form.email.data,
                        password = form.password.data
                    )
                    # Updating user's account with username
                    # Updating phone number if user chooses MFA
                    if form.phone_number.data == "":
                        auth.update_user(
                            new_user.uid,
                            display_name = form.username.data,
                            email_verified = False
                        )
                    else:
                        auth.update_user(
                            new_user.uid,
                            display_name = form.username.data,
                            phone_number = form.phone_number.data,
                            email_verified = False
                        ) 
                    # Updating realtime database to link username, email and expertise
                    user_data = {
                        "Email": form.email.data,
                        "Expertise": form.expertise.data
                    }
                    user_ref.update({form.username.data: user_data})

                    generate_otp_for_email_verification(form.email.data)

                    # Temporarily logging in user
                    session['verify'] = new_user.uid

                    return redirect(url_for('auth.verify', source = 'register'))

                # If email already exists
                except EmailAlreadyExistsError:
                    print("Register Failed! An account linked to the email already exists.")
                
                # If phone number already exists
                except PhoneNumberAlreadyExistsError:
                    print("Register Failed! An account linked to the phone number already exists.")
                    
        else:
            print("Register form incorrect: ", form.errors)

    # If an account is already logged in
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('home'))

    return render_template("temp/user_register.html", form = form)



# ---------- ORGANIZATION LOGIN ----------
@auth_blueprint.route("/org_login", methods = ["GET", "POST"])
def org_login():
    session_remove_if_not_verified()
    form = OrganizationLoginForm()

    # If no users are logged in
    if session.get("user_id") == None:
        user_ref = db.reference("/user_accounts")
        org_ref = db.reference("/org_accounts")
        
        if form.validate_on_submit():
            # Check if email is valid and exists in database
            try:
                validate_email(form.email.data)
            
                # Get org_name linked to email if it exists in the database
                org_id = auth.get_user_by_email(form.email.data).uid

                # If given org_name doesnt exist in user list and organization list
                if user_ref.child(org_id).get() == None and org_ref.child(org_id).get() == None:
                    print("An account with that email doesn't exist. Try logging in as an induvidual instead?")

                # If given org_name exists in organization list (organization account), then allow login
                if org_ref.child(org_id).get() != None:
                    if auth.get_user_by_email(form.email.data).email_verified:
                        try_login(form.email.data, form.password.data)
                    else:
                        session['verify'] = org_id
                        return redirect(url_for('auth.verify'))

                # If given org_name exists in user list (induvidual account), then prevent login from organization page
                if user_ref.child(org_id).get() != None:
                    print("An account with that email doesn't exist. Try logging in as an induvidual instead?")

            # If organization account doesnt exist in database
            except Exception as e:
                print("An account with that email doesn't exist. Try logging in as an induvidual instead?", e)

        else:
            print("Login form incorrect: ", form.errors)
    
    # If an account is already logged in
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('home'))

    return render_template("temp/org_login.html", form = form)


# ---------- ORGANIZATION REGISTER ----------
@auth_blueprint.route("/org_register", methods = ["GET", "POST"])
def org_register():
    session_remove_if_not_verified()
    form = OrganizationRegistrationForm()
    # If no accounts are logged in
    if session.get("user_id") == None:
        if form.validate_on_submit() and recaptcha.verify():
            org_ref = db.reference("/org_accounts")

            try:
                # Creating new account with email and password
                new_user = auth.create_user(
                    email = form.email.data,
                    password = form.password.data
                )
                # Updating organization's account with organization name
                auth.update_user(
                    new_user.uid,
                    display_name = form.org_name.data,
                    email_verified = False
                )

                # Updating realtime database to link org name, org website, contact person and org industry
                dictionary = {
                    "Org Website": form.company_website.data,
                    "Email": form.email.data,
                    "Contact Person Email": form.contact_person_email.data,
                    "Industry": form.industry.data
                }

                org_ref.update({new_user.uid: dictionary})

                generate_otp_for_email_verification(form.email.data)

                # Temporarily logging in user
                session['verify'] = new_user.uid

                return redirect(url_for('auth.verify', source="register"))

            # If email already exists
            except EmailAlreadyExistsError:
                print("Register Failed! An account linked to the email already exists.")

        else:
            print("Register form incorrect: ", form.errors)

    # If an account is already logged in
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('home'))

    return render_template("temp/org_register.html", form = form)

def generate_otp_for_email_verification(email):
    otp_db = db.reference("/otp")

    characters = string.ascii_letters + string.digits
    
    # Generate OTP using random.choice
    otp = ''.join(random.choice(characters) for _ in range(8))

    print(otp)

    try:
        otp_db.update({auth.get_user_by_email(email).uid: otp})
    except UserNotFoundError:
        print("User not found")

    subject = 'Email verification'
    message = 'Your OTP verification code is '+otp+"\nEnter your OTP in the website within 30 minutes to verify this email"

    sender = 'code.dev.village@gmail.com'

    body = f"Subject: {subject}\n\n{message}"

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()

    smtp.login(sender, 'jpjpoaxdwpjjoejc')

    smtp.sendmail(sender, email, body)
    smtp.quit()



@auth_blueprint.route('/temp')
def temp():
    print('before deleting', session.get('verify'))
    session_remove_if_not_verified()
    print(session.get('verify'))
    return render_template('temp/verify.html')

# Remove session if current user is unverified
# use this in the beginning of every route function
def session_remove_if_not_verified():
    if session.get('verify'):
        try:
            user = auth.get_user(session.get('verify'))
            if not user.email_verified:
                print("Deleting session verify of user", user.display_name)
                session.pop('verify', None)
        except UserNotFoundError:
            session.pop('verify', None)

    else:
        print("No session found.")


@auth_blueprint.route('/verify', methods=['GET', 'POST'])
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
            print(source)

            if source == "register":
                # Updating organization's account with organization name
                auth.update_user(
                    user_id,
                    email_verified = True
                )
                
                session.pop('verify', None)

            elif source == 'resetpass':
                return redirect(url_for('auth.reset_pass', mode='show_password'))

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


def delete_otp(user_id):
    db.reference('/otp').child(user_id).delete()

    user = auth.get_user(user_id)

    if not user.email_verified:
        auth.delete_user(user_id)
        if not db.reference("/org_accounts").child(user.uid).get():
            db.reference("/user_accounts").child(user.display_name).delete()
        else:
            db.reference("/org_accounts").child(user.uid).delete()

# Page for implementing password reset alongwith verifying email before resettin password
@auth_blueprint.route('/resetpass', methods=['GET', 'POST'])
def reset_pass():
    # if user is redirected here from login page then the mode is None, then it shows Email text field for the user to verify that the account is theirs
    # If user is redirected here from verify page then the mode is 'show_passowrd' then the display changes to password and confirm password fields
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
            return redirect(url_for('auth.verify', source = 'resetpass'))
        

    return render_template('temp/reset_pass.html', form=form, show_password_fields=display)

def is_password_valid(password):
    # Length check
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."

    # Complexity check
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*()-_=+{};:,<.>]", password):
        return False, "Password must contain at least one special character."

    # All checks passed
    return True