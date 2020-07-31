# Generates the forms for user registration.

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm, RecaptchaField  # Import our Flask Form.
from wtforms import StringField, IntegerField, PasswordField, SubmitField  # Import our field types.
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError  # Import our validators.
from flaskr.register.models import Patient, Psychiatrist  # Import our database models.

# Classes --------------------------------------------------------------------------------


class PatientRegistrationForm(FlaskForm):  # Creates a new child class, inheriting from parent 'FlaskForm'.

    username = StringField('User Name', [
        Length(min=5, max=50, message='Please enter a valid username. It is currently too long.'),
        DataRequired(message='Please enter a username.')])

    email = StringField('Email Address', [
        Length(min=2, max=100, message='Please enter a valid email address. It is currently too long.'),
        Email(message='Invalid email address.'),
        DataRequired(message='Please enter an email address.')])

    password = PasswordField('New Password', [
        Length(min=8, max=35, message='Please enter a password between 8 and 35 characters long.'),
        EqualTo('confirm_password', message='Both passwords must match'),
        DataRequired(message='Please enter a password.')])

    confirm_password = PasswordField('Confirm Password', [
        DataRequired(message='Please confirm your password.')])

    first_name = StringField('First Name', [
        Length(min=2, max=40, message='Please enter a first name between 2 and 40 characters.'),
        DataRequired(message='Please enter a first name.')])

    last_name = StringField('Last Name', [
        Length(min=2, max=80, message='Please enter a last name between 2 and 80 characters.'),
        DataRequired(message='Please enter a last name.')])

    phone_number = StringField('Phone Number', [
        Length(min=11, max=13, message='Please enter a valid phone number.'),
        DataRequired(message='Please enter a phone number.')])

    postcode = StringField('Postcode', [
        Length(min=4, max=8, message='Please enter a valid UK postcode.'),
        DataRequired(message='Please enter a postcode.')])

    medical_conditions = StringField('Medical Conditions', [
        Length(max=500, message='There is a maximum of 500 characters for this field.')])

    recaptcha = RecaptchaField()

    submit = SubmitField('Register Now!')

    def validate_patient_username(self, username):
        username_search = Patient.query.filter_by(username=username.data).first()  # Searches db for the given username.
        if username_search is not None:  # If search returns a result, raise a validation error.
            raise ValidationError('This username is already taken.')

    def validate_patient_email(self, email):
        email_search = Patient.query.filter_by(email=email.data).first()  # Searches db for the given email.
        if email_search is not None:  # If search returns a result, raise a validation error.
            raise ValidationError('An account is already registered to this email address.')


class PsychRegistrationForm(FlaskForm):  # Creates a new child class, inheriting from parent 'FlaskForm'.

    email = StringField('Email Address', [
        Length(min=2, max=100, message='Please enter a valid email address. It is currently too long.'),
        Email(message='Invalid email address.'),
        DataRequired(message='Please enter an email address.')])

    password = PasswordField('New Password', [
        Length(min=8, max=35, message='Please enter a password between 8 and 35 characters long.'),
        EqualTo('confirm_password', message='Both passwords must match'),
        DataRequired(message='Please enter a password.')])

    confirm_password = PasswordField('Confirm Password', [
        DataRequired(message='Please confirm your password.')])

    first_name = StringField('First Name', [
        Length(min=2, max=40, message='Please enter a first name between 2 and 40 characters.'),
        DataRequired(message='Please enter a first name.')])

    last_name = StringField('Last Name', [
        Length(min=2, max=80, message='Please enter a last name between 2 and 80 characters.'),
        DataRequired(message='Please enter a last name.')])

    bacp_number = IntegerField('16 Digit BACP Number', [
        Length(min=16, max=16, message='Please enter a valid 16 Digit BACP Number.'),
        DataRequired(message='You must be a certified BACP psychiatrist to register with our service.')])

    phone_number = StringField('Phone Number', [
        Length(min=11, max=13, message='Please enter a valid phone number.'),
        DataRequired(message='Please enter a phone number.')])

    postcode = StringField('Postcode', [
        Length(min=4, max=8, message='Please enter a valid UK postcode.'),
        DataRequired(message='Please enter a postcode.')])

    psychiatrist_bio = StringField('Psychiatrist Bio', [
        Length(max=500, message='Please keep your psychiatrist bio under 500 characters.'),
        DataRequired(message='Please write a short bio. This will help your patients to connect.')])

    recaptcha = RecaptchaField()

    submit = SubmitField('Register Now!')

    def validate_bacp_number(self, bacp_number):
        username_search = Psychiatrist.query.filter_by(bacp_number=bacp_number.data).first()
        if username_search is not None:  # If search returns a hit, raise a validation error.
            raise ValidationError('This bacp number has already been registered to our service.')

    def validate_psych_email(self, email):
        email_search = Psychiatrist.query.filter_by(email=email.data).first()  # Searches db for the given email.
        if email_search is not None:  # If search returns a result, raise a validation error.
            raise ValidationError('An account is already registered to this email address.')
