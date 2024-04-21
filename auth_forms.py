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
        "Cloud Computing Solutions",
        "Cybersecurity Services",
        "Data Analytics Platforms",
        "Artificial Intelligence Development",
        "Network Infrastructure Management",
        "Software as a Service (SaaS)",
        "Internet of Things (IoT) Integration",
        "DevOps Solutions",
        "Blockchain Technology Services",
        "Digital Transformation Consulting",
        "Mobile App Development",
        "Virtual Reality Solutions",
        "Augmented Reality Platforms",
        "IT Infrastructure Consulting",
        "Big Data Management",
        "Machine Learning Solutions",
        "Enterprise Resource Planning (ERP) Systems",
        "Content Management Systems (CMS)",
        "Customer Relationship Management (CRM) Software",
        "E-commerce Platforms",
        "Supply Chain Management Systems",
        "Business Intelligence Tools",
        "Cloud Storage Services",
        "Data Visualization Platforms",
        "Predictive Analytics Solutions",
        "Network Security Services",
        "Endpoint Security Solutions",
        "Identity and Access Management (IAM)",
        "Threat Intelligence Platforms",
        "Penetration Testing Services",
        "Data Loss Prevention (DLP) Solutions",
        "Vulnerability Assessment Services",
        "Incident Response Services",
        "Security Information and Event Management (SIEM)",
        "Managed Security Services",
        "Security Consulting",
        "Network Monitoring Solutions",
        "Server Management Services",
        "Data Backup and Recovery Solutions",
        "IT Disaster Recovery Planning",
        "Database Management Systems (DBMS)",
        "Data Warehousing Solutions",
        "Data Integration Services",
        "Data Governance Platforms",
        "Data Quality Management",
        "Real-time Data Processing Systems",
        "Data Lakes",
        "Data Migration Services",
        "Data Archiving Solutions",
        "Data Privacy Compliance Tools",
        "Data Encryption Services",
        "Data Masking Solutions",
        "Data Classification Systems",
        "Data Lifecycle Management",
        "Data Replication Services",
        "Cloud-Native Application Development",
        "Microservices Architecture",
        "Containerization Technologies",
        "Kubernetes Solutions",
        "Serverless Computing Platforms",
        "Continuous Integration/Continuous Deployment (CI/CD) Tools",
        "Agile Development Methodologies",
        "Test Automation Frameworks",
        "Software Testing Services",
        "Code Review and Quality Assurance",
        "Application Performance Monitoring (APM) Tools",
        "Scalability and Performance Optimization",
        "User Experience (UX) Design",
        "User Interface (UI) Development",
        "Frontend Development Frameworks",
        "Backend Development Frameworks",
        "Full-Stack Development Services",
        "Cross-Platform Development Tools",
        "Native Mobile Development",
        "Hybrid Mobile App Development",
        "Progressive Web Apps (PWAs)",
        "Mobile Backend as a Service (MBaaS)",
        "Game Development Platforms",
        "3D Modeling and Animation Software",
        "Game Engines",
        "Multiplayer Online Game Services",
        "Cloud Gaming Platforms",
        "AR/VR Game Development",
        "Game Monetization Solutions",
        "Game Analytics Tools",
        "Cloud Management Platforms",
        "Multi-Cloud Orchestration Tools",
        "Hybrid Cloud Solutions",
        "Cloud Migration Services",
        "Cloud Cost Management Tools",
        "Cloud Security Solutions",
        "Server Virtualization Technologies",
        "Desktop Virtualization Solutions",
        "Virtual Desktop Infrastructure (VDI)",
        "Application Virtualization Services",
        "Network Virtualization Technologies",
        "Storage Virtualization Solutions",
        "Security Virtualization Platforms",
        "Virtual Private Network (VPN) Services",
        "Remote Access Solutions",
        "Remote Desktop Services",
        "Remote IT Support Tools",
        "IT Service Management (ITSM) Platforms",
        "Help Desk Software",
        "Incident Management Systems",
        "Change Management Solutions",
        "Asset Management Tools",
        "Configuration Management Databases (CMDB)",
        "Service Level Agreement (SLA) Management",
        "ITIL Framework Implementation",
        "IT Governance Solutions",
        "Compliance Management Systems",
        "Risk Assessment and Management Tools",
        "Regulatory Compliance Solutions",
        "Audit and Compliance Automation",
        "IT Asset Tracking Systems",
        "Inventory Management Software",
        "License Management Tools",
        "Hardware Asset Management Solutions",
        "Software Asset Management (SAM)",
        "Network Asset Management Systems",
        "Cloud Asset Management Platforms",
        "Data Center Management Software",
        "Data Center Automation Tools",
        "Data Center Infrastructure Management (DCIM)",
        "Network Performance Monitoring (NPM) Tools",
        "Network Traffic Analysis Solutions",
        "Network Configuration Management",
        "Bandwidth Management Systems",
        "Network Optimization Tools",
        "WAN Optimization Controllers",
        "Load Balancing Solutions",
        "Content Delivery Networks (CDN)",
        "Web Application Firewalls (WAF)",
        "Intrusion Detection Systems (IDS)",
        "Intrusion Prevention Systems (IPS)",
        "Unified Threat Management (UTM) Appliances",
        "Email Security Gateways",
        "Web Security Gateways",
        "Next-Generation Firewalls (NGFW)",
        "Secure Web Gateways (SWG)",
        "Cloud Access Security Brokers (CASB)",
        "Secure Email Gateways (SEG)",
        "Mobile Device Management (MDM) Solutions",
        "Enterprise Mobility Management (EMM)",
        "Mobile Application Management (MAM)",
        "Mobile Content Management (MCM)",
        "Bring Your Own Device (BYOD) Solutions",
        "Identity Management Systems",
        "Access Management Solutions",
        "Single Sign-On (SSO) Platforms",
        "Multi-Factor Authentication (MFA)",
        "Privileged Access Management (PAM)",
        "Directory Services",
        "Password Management Tools",
        "Federated Identity Management (FIM)",
        "Role-Based Access Control (RBAC)",
        "Identity Federation Solutions",
        "Data Loss Detection and Prevention",
        "Insider Threat Detection Solutions",
        "Behavioral Analytics Tools",
        "Security Orchestration, Automation, and Response (SOAR)",
        "Threat Hunting Platforms",
        "Cloud-Native Security Solutions",
        "Container Security Platforms",
        "Server Security Software",
        "Endpoint Detection and Response (EDR)",
        "Network Segmentation Solutions",
        "Zero Trust Security Frameworks",
        "Security Information Management (SIM)",
        "Regulatory Compliance Management",
        "Privacy Management Platforms",
        "Risk Intelligence Solutions",
        "Compliance Automation Tools",
        "Security Awareness Training",
        "Disaster Recovery as a Service (DRaaS)",
        "Backup as a Service (BaaS)",
        "Replication Services",
        "High Availability Solutions",
        "Business Continuity Planning",
        "Cloud Backup Solutions",
        "Backup and Recovery Software",
        "Tape Backup Systems",
        "Continuous Data Protection (CDP)",
        "Data Replication Services",
        "Ransomware Protection Services",
        "Backup Storage Appliances",
        "Data Deduplication Solutions",
        "Virtual Tape Libraries (VTL)",
        "Email Archiving Services",
        "File Archiving Solutions",
        "Cloud Archiving Platforms",
        "Long-Term Data Storage Solutions",
        "Compliance Archiving Tools",
        "E-Discovery Software",
        "Information Governance Platforms",
        "Email Management Systems",
        "Document Management Software",
        "Digital Asset Management (DAM)",
        "Records Management Solutions"
    ])
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
    # recaptcha = RecaptchaField()

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