from flask import Flask, render_template

# Database
import firebase_admin
from firebase_admin import credentials, db, auth

# Initializing database
cred = credentials.Certificate("codebase-secret.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://codebase-93435-default-rtdb.europe-west1.firebasedatabase.app/"})

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():

    # LOGIC FOR LOGIN

    #user = auth.get_user_by_email("user@example.com")
    #print(user.uid)

    return render_template("login.html")

@app.route('/register')
def register():

    # LOGIC FOR CREATING USER

    #new_user = auth.create_user(
    #    email = "user@example.com",
    #    password = "ligma1024",
    #)

    #auth.update_user(
    #    new_user.uid,
    #    display_name = "Ligma Man",
    #    phone_number = "+971549647315",
    #    email_verified = False,
    #    photo_url = "temp photo"
    #)

    return render_template("register.html")

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




