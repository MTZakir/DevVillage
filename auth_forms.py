import re
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SelectField, StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo
import phonenumbers

# from auth_routes import is_password_valid

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

    expertise = SelectField(
        'Expertise',
        validators=[validators.DataRequired()],
        choices = [
            ('computer_systems_manager', 'Computer Systems Manager'),
            ('network_architect', 'Network Architect'),
            ('systems_analyst', 'Systems Analyst'),
            ('it_coordinator', 'IT Coordinator'),
            ('network_administrator', 'Network Administrator'),
            ('network_engineer', 'Network Engineer'),
            ('service_desk_analyst', 'Service Desk Analyst'),
            ('system_administrator', 'System Administrator'),
            ('wireless_network_engineer', 'Wireless Network Engineer'),
            ('database_administrator', 'Database Administrator'),
            ('database_analyst', 'Database Analyst'),
            ('data_quality_manager', 'Data Quality Manager'),
            ('database_report_writer', 'Database Report Writer'),
            ('sql_database_administrator', 'SQL Database Administrator'),
            ('big_data_engineer_architect', 'Big Data Engineer/Architect'),
            ('business_intelligence_specialist_analyst', 'Business Intelligence Specialist/Analyst'),
            ('business_systems_analyst', 'Business Systems Analyst'),
            ('data_analyst', 'Data Analyst'),
            ('data_analytics_developer', 'Data Analytics Developer'),
            ('data_modeling_analyst', 'Data Modeling Analyst'),
            ('data_scientist', 'Data Scientist'),
            ('data_warehouse_manager', 'Data Warehouse Manager'),
            ('data_warehouse_programming_specialist', 'Data Warehouse Programming Specialist'),
            ('intelligence_specialist', 'Intelligence Specialist'),
            ('backend_developer', 'Back-end Developer'),
            ('cloud_software_architect', 'Cloud/Software Architect'),
            ('cloud_software_developer', 'Cloud/Software Developer'),
            ('cloud_software_applications_engineer', 'Cloud/Software Applications Engineer'),
            ('cloud_system_administrator', 'Cloud System Administrator'),
            ('cloud_system_engineer', 'Cloud System Engineer'),
            ('devops_engineer', 'DevOps Engineer'),
            ('frontend_developer', 'Front-end Developer'),
            ('fullstack_developer', 'Full-stack Developer'),
            ('java_developer', 'Java Developer'),
            ('platform_engineer', 'Platform Engineer'),
            ('release_manager', 'Release Manager'),
            ('reliability_engineer', 'Reliability Engineer'),
            ('software_engineer', 'Software Engineer'),
            ('software_quality_assurance_analyst', 'Software Quality Assurance Analyst'),
            ('ui_designer', 'UI Designer'),
            ('ux_designer', 'UX Designer'),
            ('web_developer', 'Web Developer'),
            ('application_security_administrator', 'Application Security Administrator'),
            ('artificial_intelligence_security_specialist', 'Artificial Intelligence Security Specialist'),
            ('cloud_security_specialist', 'Cloud Security Specialist'),
            ('cybersecurity_hardware_engineer', 'Cybersecurity Hardware Engineer'),
            ('cyberintelligence_specialist', 'Cyberintelligence Specialist'),
            ('cryptographer', 'Cryptographer'),
            ('data_privacy_officer', 'Data Privacy Officer'),
            ('digital_forensics_analyst', 'Digital Forensics Analyst'),
            ('it_security_engineer', 'IT Security Engineer'),
            ('information_assurance_analyst', 'Information Assurance Analyst'),
            ('security_systems_administrator', 'Security Systems Administrator'),
            ('help_desk_support_specialist', 'Help Desk Support Specialist'),
            ('it_support_specialist', 'IT Support Specialist'),
            ('customer_service_representative', 'Customer Service Representative'),
            ('technical_product_manager', 'Technical Product Manager'),
            ('product_manager', 'Product Manager'),
            ('project_manager', 'Project Manager'),
            ('program_manager', 'Program Manager'),
            ('portfolio_manager', 'Portfolio Manager')
        ],
        render_kw={"class": "form-control"}  # Additional attributes for rendering the field in HTML
    )


# User login form
class UserLoginForm(FlaskForm):
    username_or_email = StringField('Username / Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    def validate_password(self, password):
        password_valid, error_msg = is_password_valid(password.data)
        if not password_valid:
            self.password.errors.append(error_msg)
        return password_valid

# Organization registration form
class OrganizationRegistrationForm(FlaskForm):
    org_name = StringField('Organization Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), validators.length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    industry = SelectField(
        'Industry',
        choices=[
            ('aircraft', 'Aircraft'),
            ('ecommerce', 'E-commerce'),
            ('other', 'Other')],
        validators=[DataRequired()])
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

def is_password_valid(password):
    # Length check
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"

    # Complexity check
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    if not re.search(r"\d", password):
        return False, "Password must contain at least one digit"
    if not re.search(r"[!@#$%^&*()\[\]_\-+=~{}|:;\"'<>,.?/]", password):
        return False, "Password must contain at least one special character"

    # All checks passed
    return True, ""