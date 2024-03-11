from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SelectMultipleField, StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
import phonenumbers

# Phone number validator
class E164PhoneNumberValidator:
    def __call__(self, form, field):
        # If phone number field is filled, perform validation
        if field.data:
            try:
                parsed_number = phonenumbers.parse(field.data)
                if not phonenumbers.is_valid_number(parsed_number):
                    print("Invalid number")
                    raise ValidationError('Invalid E.164 phone number format')
                
                print("Valid number")

            except phonenumbers.NumberParseException:
                print("Invalid number")
                raise ValidationError('Invalid E.164 phone number format')
        # If phone number field is empty, do nothing
        else:
            pass

# User registration form
class UserRegistrationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    
    username = StringField('Username', validators=[DataRequired()])
    phone_number = StringField('Phone Number', validators=[E164PhoneNumberValidator()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    
    password = PasswordField('Password', validators=[DataRequired(), validators.length(min = 8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('confirm_password', message = "Passwords do not match.")])

    expertise = SelectMultipleField(
        'Expertise',
        validators=[validators.DataRequired()],
        choices=[
            ('python', 'Python'),
            ('java', 'Java'),
            ('javascript', 'JavaScript'),
            ('ruby', 'Ruby'),
            ('csharp', 'C#')
        ],
        render_kw={"class": "form-control"}  # Additional attributes for rendering the field in HTML
    )

    recaptcha = RecaptchaField()

# User login form
class UserLoginForm(FlaskForm):
    username_or_email = StringField('Username / Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# Organization registration form
class OrganizationRegistrationForm(FlaskForm):
    org_name = StringField('Organization Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), validators.length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    industry = SelectMultipleField('Industry', choices=[('aircraft', 'Aircraft'), ('ecommerce', 'E-commerce'), ('other', 'Other')], validators=[DataRequired()])
    company_website = StringField('Company Website')
    contact_person_email = StringField('Contact Person Email', validators=[DataRequired(), Email()])

    recaptcha = RecaptchaField()

# Organization login form
class OrganizationLoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class OTPForm(FlaskForm):
    otp = StringField('OTP', validators=[DataRequired()])
    recaptcha = RecaptchaField()

class PasswordResetEmailForm(FlaskForm):
    email = StringField('Email', validators=(DataRequired(), Email()))

class PasswordResetForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired()])