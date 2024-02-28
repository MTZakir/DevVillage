from flask import Flask, render_template, session
from flask_recaptcha import ReCaptcha
from email_validator import validate_email, EmailNotValidError
from forms import UserRegistrationForm, UserLoginForm
import pyrebase

# Database
import firebase_admin
from firebase_admin import credentials, db, auth

# Initializing database
cred = credentials.Certificate("codebase-secret.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://codebase-93435-default-rtdb.europe-west1.firebasedatabase.app/"})

# Initializing flask app
app = Flask(__name__)

# Applying flask configurations     --- To be kept secret ---
app.config['SECRET_KEY'] = 'h#@hbJHB$@uygAHB!3137yugas_niGaJKH@#nlNAUBKJ~/AS,.69<>ASDfl..911,aSFOJ'
app.config['RECAPTCHA_ENABLED'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcxaoEpAAAAAH92Ayj9QRJnLO8FRHDulED4OZOY'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcxaoEpAAAAAEOeRtpgYt_PDprYUmkVw_ryUl2p'

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
recaptcha = ReCaptcha(app)


# HOME
@app.route('/')
def index():
    return render_template("index.html")


# ---------- TESTING -----------------------------

@app.route('/check')
def check():
    print(session.get('user_id'))
    return render_template('homecomp.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return render_template('homecomp.html')

# ------------------------------------------------

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()

    if form.validate_on_submit():
        # If input is email
        try:
            validate_email(form.username_or_email.data)
            try_login(form.username_or_email.data, form.password.data)

        # If input is username
        except:
            account_ref = db.reference("/users")
            
            if account_ref.get() != None:
                # Get email linked to specified username if it exists
                try:
                    user_email = account_ref.child(form.username_or_email.data).get()

                    try_login(user_email, form.password.data)
                except:
                    print("An account with that username / email doesn't exist.")
            else:
                print("User list is empty.")

    else:
        print("Login form incorrect: ", form.errors)

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
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()

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
            ref.update({form.username.data: form.email.data})


    else:
        print("Register form incorrect: ", form.errors)

    return render_template("temp/user_register.html", form = form)


# DISCOVER
@app.route('/discover')
def discover():

    # LOGIC FOR DISCOVER

    #ref = db.reference("/users")
    #ref.update({"Chupapi": {"age": "6", "ball size": "2mm", "ball height": "0.1mm"}})

    return render_template("discover.html")


@app.route('/home')
def homecomp():
    return render_template("homecomp.html")


if __name__ == '__main__':
    app.run(debug=True)




