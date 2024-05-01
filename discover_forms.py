from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, DecimalField, FileField, validators
from wtforms.validators import DataRequired, NumberRange, Optional
from firebase_admin import db, auth
from decimal import Decimal
import pyrebase


class CreateContract(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    min_price = StringField('Minimum Price', validators=[DataRequired(), validators.Regexp(r'^[0-9]+(?:\.[0-9]+)?$', message = "Please enter a valid number")])
    max_price = StringField('Maximum Price', validators=[DataRequired(), validators.Regexp(r'^[0-9]+(?:\.[0-9]+)?$', message = "Please enter a valid number")])
    duration = SelectField(
        'Duration',
        choices=[
            ('15', '15 Days'),
            ('30', '1 Month'),
            ('45', '1 Month + 15 Days'),
            ('60', '2 Months'),
            ('75', '2 Months + 15 Days'),
            ('90', '3 Months'),
        ],
        validators=[DataRequired()]
        )
    difficulty = SelectField(
        'Select Difficulty',
        choices=[
            'Beginner',
            'Intermediate',
            'Advanced',
            'Expert',
            'Master',
        ],
        validators=[DataRequired()]
    )
    contract_img = FileField('Contract Image', validators=[Optional(), FileAllowed(['jpg', 'jpeg', 'png'], message = 'Images only!')])
    scope = StringField('Scope of Work', validators=[DataRequired()])
    deliverables = StringField('Deliverables', validators=[DataRequired()])
    tech_stack = StringField('Technology Stack', validators=[DataRequired()])
    notes = StringField('Additional Notes', validators=[Optional()])

class ApplyContract(FlaskForm):
    pay_range = DecimalField('Pay Range', validators=[DataRequired()])
    capability = SelectField(
        'How would you rate your level of expertise for this contract?',
        choices=[
            ('1', 'Novice - Just starting out.'),
            ('2', 'Apprentice - Building skills and gaining experience.'),
            ('3', 'Seasoned - Proficient and capable.'),
            ('4', 'Expert - Highly skilled and experienced.'),
            ('5', 'Master - A true authority in the field.')
        ],
        validators=[DataRequired()]
    )
    message = StringField('Type a message to the company.', validators=[DataRequired()])
    resume = FileField('Upload your resume', validators=[DataRequired(), FileAllowed(['pdf'], 'Only PDF files are allowed!')])

    def __init__(self, contract_id, user_id, *args, **kwargs):
        super(ApplyContract, self).__init__(*args, **kwargs)

        # Setting cap for pay_range
        # Min range is same
        self.min_price = int(db.reference("/contracts").child(contract_id).get()["Min Price"])
        # Max range is 20% more than default + its set to closest increment of 50
        self.max_price = int(round(float(db.reference("/contracts").child(contract_id).get()["Max Price"]) * 1.2 / 50)) * 50

        # Convert pay_range value to an integer
        if 'pay_range' in kwargs and kwargs['pay_range']:
            self.pay_range.data = int(Decimal(kwargs['pay_range']))

        self.pay_range.validators.append(NumberRange(min = self.min_price, max = self.max_price))

        # Resume submission
        username = auth.get_user(user_id).display_name
        user = db.reference("/user_accounts").child(username).get()
        # If user already has resume in account, delete resume field
        if "Resume" in user:
            delattr(self, 'resume')


class ApplicantAcceptReject(FlaskForm):
    applicant = StringField("Applicant", validators=[DataRequired()])
    contract = StringField("Contract", validators=[DataRequired()])