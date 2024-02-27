from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, ValidationError
import phonenumbers

# Phone number validator
class E164PhoneNumberValidator:
    def __call__(self, form, field):
        try:
            parsed_number = phonenumbers.parse(field.data)
            if not phonenumbers.is_valid_number(parsed_number):
                print("Invalid number")
                raise ValidationError('Invalid E.164 phone number format')
            
            print("Valid number")

        except phonenumbers.NumberParseException:
            print("Invalid number")
            raise ValidationError('Invalid E.164 phone number format')

# User registration form
class UserRegistrationForm(FlaskForm):
        first_name = StringField('First Name', validators=[DataRequired()])
        last_name = StringField('Last Name', validators=[DataRequired()])
        
        username = StringField('Username', validators=[DataRequired()])
        phone_number = StringField('Phone Number', validators=[DataRequired(), E164PhoneNumberValidator()])
        email = StringField('Email', validators=[DataRequired(), Email()])
        
        password = PasswordField('Password', validators=[DataRequired(), validators.length(min = 8)])
        confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])

        recaptcha = RecaptchaField()