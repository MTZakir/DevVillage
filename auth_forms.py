import re
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import SelectField, SelectMultipleField, StringField, PasswordField, validators
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, URL, Optional
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
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message = "Passwords do not match.")])

    expertise = SelectMultipleField(
        'Expertise',
        choices = [
        ".NET Core (C#)",
        "Agile Coaching and Mentoring",
        "Agile Collaboration Tools",
        "Agile Estimation Techniques",
        "Agile Methodologies Implementation",
        "Agile Portfolio Management",
        "Agile Product Backlog Management",
        "Agile Product Ownership",
        "Agile Project Management",
        "Agile Release Management",
        "Agile Requirements Gathering",
        "Agile Retrospective Facilitation",
        "Agile Scrum Mastering",
        "Agile Sprint Planning",
        "Agile Team Facilitation",
        "Agile Team Leadership",
        "Agile Transformation",
        "AI-driven Automation",
        "Angular (JavaScript/TypeScript)",
        "API Gateway Management",
        "API Lifecycle Management",
        "API Security Best Practices",
        "API Security",
        "Application Security Testing",
        "Axios",
        "Big Data Analytics",
        "Blockchain Development",
        "Blockchain Implementation",
        "Business Continuity Planning",
        "Business Intelligence Reporting",
        "C#",
        "C++",
        "Chatbot Development",
        "Cloud Architecture",
        "Cloud Compliance Management",
        "Cloud Cost Management",
        "Cloud Cost Optimization",
        "Cloud Data Encryption",
        "Cloud Governance Frameworks",
        "Cloud Identity Management",
        "Cloud Migration Planning",
        "Cloud Platform SDKs",
        "Cloud Resource Optimization",
        "Cloud Security Architecture",
        "Cloud Security Governance",
        "Cloud Security Monitoring",
        "Cloud Service Level Agreement (SLA) Management",
        "Cloud Service Management",
        "Cloud Service Orchestration",
        "Cloud-based Data Management",
        "Cloud-based Disaster Recovery Planning",
        "Cloud-native Application Development",
        "Cloud-native Data Replication",
        "Cloud-native Database Management",
        "Cloud-native Development",
        "Cloud-native Infrastructure Design",
        "Cloud-native Monitoring",
        "Cloud-native Security",
        "Container Orchestration",
        "Container Security",
        "Continuous Delivery Practices",
        "Continuous Deployment",
        "Continuous Integration Practices",
        "Cross-functional Collaboration",
        "Cross-platform Development",
        "Cucumber Testing",
        "Cyber Threat Intelligence",
        "Cybersecurity Analysis",
        "Data Center Management",
        "Data Center Security",
        "Data Center Virtualization",
        "Data Engineering",
        "Data Governance Framework Implementation",
        "Data Governance Frameworks",
        "Data Governance Policies",
        "Data Lake Architecture",
        "Data Lifecycle Management",
        "Data Loss Prevention",
        "Data Masking Techniques",
        "Data Migration Strategies",
        "Data Privacy Compliance",
        "Data Privacy Impact Assessment",
        "Data Privacy Policy Development",
        "Data Profiling Techniques",
        "Data Replication Strategies",
        "Data Visualization Techniques",
        "Data Warehousing",
        "Data-driven Decision Making",
        "Data-driven Marketing Analytics",
        "Data-driven Performance Optimization",
        "Data-driven Product Development",
        "Data-driven UX Design",
        "Database Optimization",
        "Datacenter Consolidation",
        "DevSecOps",
        "Digital Forensics",
        "Distributed Systems Architecture",
        "Docker",
        "Enterprise Architecture Design",
        "Flask (Python)",
        "Frontend Optimization",
        "Full Stack Development",
        "Git",
        "Go",
        "Hibernate (Java)",
        "HTML/CSS",
        "Identity Access Management (IAM)",
        "Incident Response Management",
        "Information Security Auditing",
        "Infrastructure as Code (IaC)",
        "Infrastructure Automation",
        "Infrastructure Monitoring",
        "IoT Solutions Architecture",
        "IT Architecture Governance",
        "IT Asset Discovery",
        "IT Asset Management",
        "IT Change Management",
        "IT Compliance Auditing",
        "IT Financial Management",
        "IT Governance",
        "IT Incident Management",
        "IT Incident Response Planning",
        "IT Infrastructure Planning",
        "IT Infrastructure Security",
        "IT Policy Development",
        "IT Portfolio Management",
        "IT Procurement Management",
        "IT Project Portfolio Management",
        "IT Risk Assessment",
        "IT Security Governance",
        "IT Service Catalog Management",
        "IT Service Continuity Management",
        "IT Service Cost Management",
        "IT Service Delivery Optimization",
        "IT Service Desk Automation",
        "IT Service Desk Management",
        "IT Service Desk Optimization",
        "IT Service Level Management",
        "IT Service Request Management",
        "IT Strategy Development",
        "IT Vendor Management",
        "ITIL Process Implementation",
        "Java",
        "JavaScript",
        "JUnit (Java)",
        "Kotlin",
        "Machine Learning Engineering",
        "Mobile Application Design",
        "Mobile Application Development Frameworks",
        "Mobile Application Lifecycle Management",
        "Mobile Application Performance Optimization",
        "Mobile Application Security Testing",
        "Mobile Application Security",
        "Mobile Application Testing",
        "Mobile Application Usability Testing",
        "Mobile Development Frameworks",
        "Mobile Device Management (MDM)",
        "Multi-cloud Strategy",
        "MySQL",
        "Natural Language Processing (NLP)",
        "Network Access Control",
        "Network Anomaly Detection",
        "Network Automation",
        "Network Capacity Planning",
        "Network Intrusion Prevention",
        "Network Load Balancing",
        "Network Packet Inspection",
        "Network Performance Optimization",
        "Network Protocol Analysis",
        "Network Security Analysis",
        "Network Segmentation",
        "Network Segregation",
        "Network Threat Detection",
        "Network Traffic Analysis",
        "Network Traffic Shaping",
        "Network Vulnerability Scanning",
        "Node.js (JavaScript)",
        "Penetration Testing",
        "Perl",
        "PHP",
        "Play Framework (Java/Scala)",
        "Predictive Analytics Modeling",
        "Python",
        "React.js (JavaScript)",
        "Redux",
        "Risk Management Frameworks",
        "Ruby on Rails (Ruby)",
        "Ruby",
        "Scala",
        "Scalable System Design",
        "Secure Access Management",
        "Secure API Design",
        "Secure Cloud Storage Solutions",
        "Secure Coding Practices",
        "Secure DevOps Practices",
        "Secure Network Architecture Design",
        "Secure Network Design",
        "Secure SDLC",
        "Secure Software Development Lifecycle",
        "Secure Software Development",
        "Secure Web Application Development",
        "Security Incident Handling",
        "Serverless Application Development",
        "Serverless Architecture Patterns",
        "Serverless Computing",
        "Social Engineering Awareness",
        "Software Deployment Automation",
        "Software Quality Assurance",
        "Spring Framework (Java)",
        "Swift",
        "Systems Integration",
        "TensorFlow",
        "Threat Modeling",
        "TypeScript",
        "User Experience Optimization",
        "User Interface Design Patterns",
        "User Story Mapping",
        "User-Centric Design",
        "UX Copywriting",
        "UX Research and Testing",
        "UX/UI Prototyping",
        "Varnish",
        "Voice User Interface (VUI) Design",
        "Web Content Management",
        "Web Performance Tuning"
    ],
    render_kw={"class": "form-control"}  # Additional attributes for rendering the field in HTML 
    )
    
    def validate_password(self, password):
        password_valid, error_msg = is_password_valid(password.data)
        if not password_valid:
            self.password.errors.append(error_msg)
        return password_valid
    
    def validate_email(self, email):
        email_valid, error_msg = is_email_valid(email.data)
        if not email_valid:
            self.email.errors.append(error_msg)
        return email_valid


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
    industry = SelectMultipleField(
        'Industry',
        choices=[
            ('aircraft', 'Aircraft'),
            ('ecommerce', 'E-commerce'),
            ('other', 'Other')])
    company_website = StringField('Company Website', validators=[Optional(), URL(require_tld=True, message='Invalid URL')])
    contact_person_email = StringField('Contact Person Email', validators=[DataRequired(), Email()])

    def validate_password(self, password):
        password_valid, error_msg = is_password_valid(password.data)
        if not password_valid:
            self.password.errors.append(error_msg)
        return password_valid

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

def is_email_valid(email):
    # Regular expression pattern for validating email addresses
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if email matches the pattern
    if not re.match(pattern, email):
        return False, "Invalid email address"
    
    # Split email address into local part and domain part
    local_part, domain_part = email.split('@')

    # Check length of local part
    if len(local_part) > 64:
        return False, "Local part exceeds maximum length (64 characters)"
    
    # Check length of domain part
    if len(domain_part) > 255:
        return False, "Domain part exceeds maximum length (255 characters)"
    
    # Check if domain has valid characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', domain_part):
        return False, "Domain contains invalid characters"
    
    # Check if domain starts or ends with a dot
    if domain_part.startswith('.') or domain_part.endswith('.'):
        return False, "Domain cannot start or end with a dot"

    # Split the domain into parts
    domain_parts = domain_part.split('.')
    # Check if the last part (TLD) has at least two characters
    if len(domain_parts[-1]) < 2:
        return False, "Invalid Top-Level Domain (TLD)"
    
    return True, "Email is valid"