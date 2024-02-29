from email_validator import validate_email
from flask import Blueprint, render_template, session, redirect, url_for
from firebase_admin import db, auth
from flask_recaptcha import ReCaptcha
from forms import OrgLoginForm, OrganizationRegistrationForm, UserLoginForm, UserRegistrationForm
import pyrebase

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
    print(session.get('user_id'))
    return render_template('homecomp.html')

@auth_blueprint.route('/logout')
def logout():
    session.pop('user_id', None)
    print("User logged out")
    return render_template('homecomp.html')

# ------------------------------------------------

# LOGIN
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if session.get("user_id") == None:
        account_ref = db.reference("/users")
        
        if form.validate_on_submit():
            # If input is email
            try:
                validate_email(form.username_or_email.data)

                username = auth.get_user_by_email(form.username_or_email.data).display_name

                try:
                    email_check = account_ref.child(username).get()
                    try_login(form.username_or_email.data, form.password.data)
                
                except:
                    print("An account with that email doesn't exist. Try logging in as an organization instead")

            # If input is username
            except Exception as e:
                
                if account_ref.get() != None:
                    # Get email linked to specified username if it exists
                    try:
                        user_email = account_ref.child(form.username_or_email.data).child("Email").get()

                        try_login(user_email, form.password.data)
                    except:
                        print("An account with that username / email doesn't exist. Try logging in as an organization instead", e)
                else:
                    print("User list is empty.")

        else:
            print("Login form incorrect: ", form.errors)
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('index'))

    return render_template("temp/user_login.html", form = form)

# Function to authorize users with firebase
def try_login(user_email, user_pass):
    try:
        pyre_auth.sign_in_with_email_and_password(user_email, user_pass)

        user_id = auth.get_user_by_email(user_email).uid

        session['user_id'] = user_id

        print("SUCCESSFULLY LOGGED IN!")
    except:
        print("Incorrect username/email or password.")


# USER REGISTER
@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()
    if session.get("user_id") == None:
        if form.validate_on_submit() and recaptcha.verify():
            ref = db.reference("/users")

            if ref.get() != None and form.username.data in ref.get():
                print("Username already exists")
            else:
                # Creating new user with email and password
                new_user = auth.create_user(
                    email = form.email.data,
                    password = form.password.data
                )
                # Updating user's account with username and phone number
                auth.update_user(
                    new_user.uid,
                    display_name = form.username.data,
                    phone_number = form.phone_number.data,
                    email_verified = False
                )
                # Updating realtime database to link username and email
                dictionary = {"Email": form.email.data,
                            "Expertise": form.expertise.data}
                
                ref.update({form.username.data: dictionary})

        else:
            print("Register form incorrect: ", form.errors)
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('index'))

    return render_template("temp/user_register.html", form = form)

# Organisation registration and login route functions

@auth_blueprint.route("/orgregister", methods = ["GET", "POST"])
def orgregister():
    form = OrganizationRegistrationForm()
    if session.get("user_id") == None:
        if form.validate_on_submit() and recaptcha.verify():
            ref = db.reference("/org_accounts")

            if ref.get() == None:
                # Creating new user with email and password
                new_user = auth.create_user(
                    email = form.email.data,
                    password = form.password.data
                )
                # Updating user's account with username and phone number
                auth.update_user(
                    new_user.uid,
                    display_name = form.org_name.data,
                    email_verified = False
                )
                # Updating realtime database to link username and email
                dictionary = {"Org Website": form.company_website.data, "Contact Person Email": form.contact_person_email.data, "Industry": form.industry.data}
                
                ref.update({form.org_name.data: dictionary})

        else:
            print("Register form incorrect: ", form.errors)
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('index'))

    return render_template("temp/org_register.html", form = form)

@auth_blueprint.route("/orgsignin", methods = ["GET", "POST"])
def orgsignin():
    form = OrgLoginForm()

    return render_template("temp/org_login.html", form = form)
