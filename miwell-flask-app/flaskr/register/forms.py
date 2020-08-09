# Generates the forms for user registration.

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm  # Import our Flask Form.
from wtforms import StringField, PasswordField, SubmitField, TextAreaField  # Import our field types.
from wtforms.validators import DataRequired, EqualTo, Length, Email, ValidationError  # Import our validators.
from wtforms_validators import Integer

from flaskr import db
from flaskr.register.models import Patient, Psychiatrist  # Import our database models.

# Classes --------------------------------------------------------------------------------


class PatientRegistrationForm(FlaskForm):  # Creates a new child class, inheriting from parent 'FlaskForm'.

    username = StringField('User Name', [
        Length(min=5, max=50, message='Please enter a different username.'),
        DataRequired(message='Please enter a username.')])

    email = StringField('Email Address', [
        Length(min=2, max=100, message='Please enter a valid email address.'),
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

    medical_conditions = TextAreaField('Medical Conditions', [
        Length(max=500, message='There is a maximum of 500 characters for this field.')])

    # recaptcha = RecaptchaField()

    submit = SubmitField('Register Now!')

    # Custom Validators ---------------------------------------------------------------------

    # Search for any patients within the database that have an identical username or email.

    def validate_username(self, username):
        patient_username = db.session.query(Patient).filter(Patient.username == username.data).first()

        if patient_username:
            raise ValidationError('A psychiatrist has already registered with this BACP number.')

    def validate_email(self, email):
        psych_email = db.session.query(Psychiatrist).filter(Psychiatrist.email == email.data).first()
        patient_email = db.session.query(Patient).filter(Patient.email == email.data).first()

        if psych_email or patient_email:
            raise ValidationError('An account already exists with the current email address.')


class PsychRegistrationForm(FlaskForm):  # Creates a new child class, inheriting from parent 'FlaskForm'.

    email = StringField('Email Address', [
        Length(min=2, max=100, message='Please enter a valid email address.'),
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

    bacp_number = StringField('16 Digit BACP Number', [
        Length(min=16, max=16, message='Please enter a valid 16 Digit BACP Number.'),
        DataRequired(message='You must be a certified BACP psychiatrist to register with our service.'),
        Integer(message='The BACP Number can only consist of numbers!')])

    phone_number = StringField('Phone Number', [
        Length(min=11, max=13, message='Please enter a valid phone number.'),
        DataRequired(message='Please enter a phone number.')])

    postcode = StringField('Postcode', [
        Length(min=4, max=8, message='Please enter a valid UK postcode.'),
        DataRequired(message='Please enter a postcode.')])

    psychiatrist_bio = TextAreaField('Psychiatrist Bio', [
        Length(max=500, message='Please keep your psychiatrist bio under 500 characters.'),
        DataRequired(message='Please write a short bio. This will help your patients to connect.')])

    # recaptcha = RecaptchaField()

    submit = SubmitField('Register Now!')

    # Custom Validators ---------------------------------------------------------------------

    # Search for any psychiatrists within the database that have an identical BACP number or email.

    def validate_bacp_number(self, bacp_number):
        psychiatrist_bacp = db.session.query(Psychiatrist).\
            filter(Psychiatrist.bacp_number == bacp_number.data).first()

        if psychiatrist_bacp:
            raise ValidationError('A psychiatrist has already registered with this BACP number.')

    def validate_email(self, email):

        psych_email = db.session.query(Psychiatrist).filter(Psychiatrist.email == email.data).first()
        patient_email = db.session.query(Patient.email).filter_by(Patient.email == email.data).first()

        if psych_email or patient_email:
            raise ValidationError('An account already exists with the current email address.')