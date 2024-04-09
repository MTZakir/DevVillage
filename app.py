from flask import Flask, render_template, request, session
from auth_routes import auth_blueprint
from discover_routes import discover_blueprint
from dashboard_routes import dashboard_blueprint
from verify_routes import verify_blueprint
from profile_routes import prof_blueprint
from firebase_admin import auth
from firebase_admin._auth_utils import UserNotFoundError

# Database
import firebase_admin
from firebase_admin import credentials

# Initializing database
cred = credentials.Certificate("codebase-secret.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://codebase-93435-default-rtdb.europe-west1.firebasedatabase.app/"})

# Initializing flask app
app = Flask(__name__)
app.register_blueprint(auth_blueprint)
app.register_blueprint(discover_blueprint)
app.register_blueprint(dashboard_blueprint)
app.register_blueprint(verify_blueprint)
app.register_blueprint(prof_blueprint)

# Remove session if current user is unverified
def session_remove_if_not_verified():
    # Exclude the 'verify' route function
    if request.endpoint != 'auth.verify':
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

# Applying flask configurations     --- To be kept secret ---
app.config['SECRET_KEY'] = 'h#@hbJHB$@uygAHB!3137yugas_niGaJKH@#nlNAUBKJ~/AS,.69<>ASDfl..911,aSFOJ'
app.config['RECAPTCHA_ENABLED'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcxaoEpAAAAAH92Ayj9QRJnLO8FRHDulED4OZOY'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcxaoEpAAAAAEOeRtpgYt_PDprYUmkVw_ryUl2p'
app.config['RECAPTCHA_THEME'] = 'dark'

# TEMP DICT VALUES FOR DISCOVER PAGE

# HOME
@app.route('/')
def home():
    session_remove_if_not_verified()
    return render_template("home.html")

@app.route('/homecomp')
def homecomp():
    session_remove_if_not_verified()
    return render_template("homecomp.html")


if __name__ == '__main__':
    app.run(debug=True)

