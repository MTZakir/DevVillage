from flask import Flask, render_template
from flask_recaptcha import ReCaptcha
from forms import UserRegistrationForm

# Database
import firebase_admin
from firebase_admin import credentials, db, auth

# Initializing database
cred = credentials.Certificate("codebase-secret.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://codebase-93435-default-rtdb.europe-west1.firebasedatabase.app/"})

app = Flask(__name__)

app.config['SECRET_KEY'] = 'h#@hbJHB$@uygAHB!3137yugas_niGaJKH@#nlNAUBKJ~/AS,.69<>ASDfl..911,aSFOJ'
app.config['RECAPTCHA_ENABLED'] = True
app.config['RECAPTCHA_SITE_KEY'] = '6LcxaoEpAAAAAH92Ayj9QRJnLO8FRHDulED4OZOY'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcxaoEpAAAAAEOeRtpgYt_PDprYUmkVw_ryUl2p'

recaptcha = ReCaptcha(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():

    # LOGIC FOR LOGIN

    #user = auth.get_user_by_email("user@example.com")
    #print(user.uid)

    return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserRegistrationForm()

    if form.validate_on_submit():
        # If captcha failed
        #if not recaptcha.verify():
        #    print("ReCaptcha failed.")
        # If captcha success
        #else:
            # If password != confirm password
        if form.password != form.confirm_password:
            print("Passwords do no match.")
        
        new_user = auth.create_user(
            email = form.email.data,
            password = form.password.data
        )

        auth.update_user(
            new_user.uid,
            display_name = form.username.data,
            phone_number = form.phone_number.data,
            email_verified = False
        )

    return render_template("temp_HTML/user_register.html", form = form)

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




