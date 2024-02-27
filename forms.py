from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class UserRegistrationForm(FlaskForm):
        first_name = StringField('First Name', validators=[DataRequired()])
        last_name = StringField('Last Name', validators=[DataRequired()])
        
        username = StringField('Username', validators=[DataRequired()])
        phone_number = StringField('Phone Number', validators=[DataRequired()])
        email = StringField('Email', validators=[DataRequired(), Email()])
        
        password = PasswordField('Password', validators=[DataRequired()])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])

        repatcha = RecaptchaField()