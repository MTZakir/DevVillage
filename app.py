from flask import Flask, render_template, session
from auth_routes import auth_blueprint, session_remove_if_not_verified
from discover_routes import discover_blueprint
from dashboard_routes import dashboard_blueprint

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

# Applying flask configurations     --- To be kept secret ---
app.config['SECRET_KEY'] = 'h#@hbJHB$@uygAHB!3137yugas_niGaJKH@#nlNAUBKJ~/AS,.69<>ASDfl..911,aSFOJ'
app.config['RECAPTCHA_ENABLED'] = True
app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcxaoEpAAAAAH92Ayj9QRJnLO8FRHDulED4OZOY'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcxaoEpAAAAAEOeRtpgYt_PDprYUmkVw_ryUl2p'

# HOME
@app.route('/')
def home():
    session_remove_if_not_verified()
    return render_template("home.html")

@app.route('/home')
def homecomp():
    session_remove_if_not_verified()
    return render_template("homecomp.html")


if __name__ == '__main__':
    app.run(debug=True)




