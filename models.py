from app import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Users table
class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    pfp = db.Column(db.String(1000), nullable = False)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(), nullable = False)

    def __repr__(self):
        return self.username

    # Function to set password (For Register)
    def set_pass(self, user_pass):
        self.password = bcrypt.generate_password_hash(user_pass).decode('utf-8')

    # Function to verify password (For Login)
    def check_pass(self, user_pass):
        return bcrypt.check_password_hash(self.password, user_pass)