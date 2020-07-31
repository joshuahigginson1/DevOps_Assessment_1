"""
A template which lays out the basic syntax for a forms.py file using Flask and WTForms.
"""

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm, RecaptchaField  # Import our Flask Form.
from wtforms import StringField, SubmitField  # Import our field types.
from wtforms.validators import DataRequired, Length, Email  # Import our validators.


# Classes --------------------------------------------------------------------------------


class NewForm(FlaskForm):  # Creates a child class called 'NewForm', inheriting from parent 'FlaskForm'.

    name = StringField('Name', [
        DataRequired()])

    email = StringField('Email', [
        Email(message='Not a valid email address.'),
        DataRequired()])
    body = StringField('Message', [
        DataRequired(),
        Length(min=4, message='Your message is too short.')])

    recaptcha = RecaptchaField()

    submit = SubmitField('Submit')

# Validator Syntax:
# VARIABLE = FIELD_TYPE('FIELD_NAME', [ # list of validators.
# VALIDATOR_TYPE(message=('ERROR_MESSAGE'),
# VALIDATOR_TYPE(message=('ERROR_MESSAGE')
# )])
