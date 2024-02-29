from email_validator import validate_email
from flask import Blueprint, render_template, session, redirect, url_for
from firebase_admin import db, auth
from firebase_admin._auth_utils import EmailAlreadyExistsError, PhoneNumberAlreadyExistsError
from flask_recaptcha import ReCaptcha
from forms import OrganizationLoginForm, OrganizationRegistrationForm, UserLoginForm, UserRegistrationForm
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
                    try_login(form.username_or_email.data, form.password.data)

                # If given username exists in organization list (organization account), then prevent login from induvidual page
                if org_ref.child(username).get() != None:
                    print("An account with that email doesn't exist. Try logging in as an organization instead?")

            # If input is username
            except Exception as e:
                
                if user_ref.get() != None:
                    # Get email linked to specified username if it exists
                    try:
                        user_email = user_ref.child(form.username_or_email.data).child("Email").get()

                        try_login(user_email, form.password.data)

                    except:
                        print("An account with that email doesn't exist. Try logging in as an organization instead?", e)
                else:
                    print("User list is empty.")

        else:
            print("Login form incorrect: ", form.errors)
        
    # If a user is already logged in
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('index'))

    return render_template("temp/user_login.html", form = form)


# ---------- USER REGISTER ----------
@auth_blueprint.route('/user_register', methods=['GET', 'POST'])
def user_register():
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

        return redirect(url_for('index'))

    return render_template("temp/user_register.html", form = form)



# ---------- ORGANIZATION LOGIN ----------
@auth_blueprint.route("/org_login", methods = ["GET", "POST"])
def org_login():
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
                org_name = auth.get_user_by_email(form.email.data).display_name

                # If given org_name doesnt exist in user list and organization list
                if user_ref.child(org_name).get() == None and org_ref.child(org_name).get() == None:
                    print("An account with that email doesn't exist. Try logging in as an induvidual instead?")

                # If given org_name exists in organization list (organization account), then allow login
                if org_ref.child(org_name).get() != None:
                    try_login(form.email.data, form.password.data)

                # If given org_name exists in user list (induvidual account), then prevent login from organization page
                if user_ref.child(org_name).get() != None:
                    print("An account with that email doesn't exist. Try logging in as an induvidual instead?")

            # If organization account doesnt exist in database
            except Exception as e:
                print("An account with that email doesn't exist. Try logging in as an induvidual instead?", e)

        else:
            print("Login form incorrect: ", form.errors)
    
    # If an account is already logged in
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('index'))

    return render_template("temp/org_login.html", form = form)




# ---------- ORGANIZATION REGISTER ----------
@auth_blueprint.route("/org_register", methods = ["GET", "POST"])
def org_register():
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
                    "Contact Person Email": form.contact_person_email.data,
                    "Industry": form.industry.data
                }
                org_ref.update({form.org_name.data: dictionary})

            # If email already exists
            except EmailAlreadyExistsError:
                print("Register Failed! An account linked to the email already exists.")

        else:
            print("Register form incorrect: ", form.errors)

    # If an account is already logged in
    else:
        print(session.get("user_id"), "is already logged in.")

        return redirect(url_for('index'))

    return render_template("temp/org_register.html", form = form)
