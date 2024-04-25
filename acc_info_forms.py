from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email, Optional

class WalletTopup(FlaskForm):
    amount = StringField("Amount", validators = [DataRequired()])

class BuyTokens(FlaskForm):
    token = StringField("Token", validators = [DataRequired()])

class AccountInfo(FlaskForm):
    first_name = StringField("First Name", validators = [Optional()])
    last_name = StringField("Last Name", validators = [Optional()])
    email = StringField("Last Name", validators = [Optional(), Email()])
    display_name = StringField("Display Name", validators = [Optional()])
    phone = StringField("Phone Number", validators = [Optional()])
    expertise = StringField("Fields of expertise", validators = [Optional()])
    password = StringField("Password", validators = [Optional()])
    dob = StringField("Date of Birth", validators = [Optional()])
    gender = SelectField("Gender",
                         choices=["Male", "Female"],
                         validators = [Optional()])
    bio = StringField("Bio", validators = [Optional()])