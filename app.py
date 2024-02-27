from flask import Flask, render_template
from flask_recaptcha import ReCaptcha
from forms import UserRegistrationForm

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

# Initialize recaptcha
recaptcha = ReCaptcha(app)


# HOME
@app.route('/')
def index():
    return render_template("index.html")

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    # LOGIC FOR LOGIN

    #user = auth.get_user_by_email("user@example.com")
    #print(user.uid)

    return render_template("login.html")

# USER REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()

    if form.validate_on_submit() and recaptcha.verify():
        # If password != confirm password
        if form.password.data != form.confirm_password.data:
            print("Passwords do no match.")
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
    else:
        print("Form incorrect!")

    return render_template("temp_HTML/user_register.html", form = form)


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




