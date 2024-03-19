from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, validators
from wtforms.validators import DataRequired

from firebase_admin import db


class CreateContract(FlaskForm):
    min_price = StringField('Minimum Price', validators=[DataRequired(), validators.Regexp(r'^[0-9]+(?:\.[0-9]+)?$', message = "Please enter a valid number")])
    max_price = StringField('Maximum Price', validators=[DataRequired(), validators.Regexp(r'^[0-9]+(?:\.[0-9]+)?$', message = "Please enter a valid number")])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    contract_img = StringField('Contract URL', validators=[DataRequired()])
    #contract_img = FileField('Contract Image', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'], message = 'Images only!')])

