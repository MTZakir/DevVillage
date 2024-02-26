from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm
from flask_wtf.csrf import CSRFProtect

# Creating flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'h#@hbJHB$@uygAHB!3137yugas_niGaJKH@#nlNAUBKJ~/AS,.69<>ASDfl..911,aSFOJ'

# Initializing database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///codebase.db'
#app.app_context().push()    # Idk wat this does but db table "CREATION" only works with this
db = SQLAlchemy(app)
from models import Users


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")


# TEMP REGISTER ------------------------------------------
@app.route('/temp', methods=['GET', 'POST'])
def temp_register():
    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = Users(pfp = 'temp',
                        first_name = form.first_name.data,
                        last_name = form.last_name.data,
                        username = form.username.data,
                        email = form.email.data)
        new_user.set_pass(form.password.data)
        db.session.add(new_user)
        db.session.commit()

        print(f"Successfully added the user {form.username.data}.")

    return render_template("temp.html", form = form)

# ---------------------------------------------------------


@app.route('/discover')
def discover():
    return render_template("discover.html")

@app.route('/home')
def homecomp():
    return render_template("homecomp.html")

if __name__ == '__main__':
    app.run(debug=True)