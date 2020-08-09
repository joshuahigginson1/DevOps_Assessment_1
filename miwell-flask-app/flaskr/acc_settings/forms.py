# A script which manages our account update and deletion forms.

# Imports ------------------------------------------------------------------------

from flask_login import current_user
from flask_argon2 import check_password_hash
from flaskr.register.models import Patient, Psychiatrist

from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, Length, EqualTo

# Forms -------------------------------------------------------------------------

# A base form class, where other forms can inherit our custom validation.


class AccountSettingFormBase(FlaskForm):

    # Custom Validators ----------------------------------------------------------

    def validate_email(self):

        # here, we check to see that there are no duplicate emails within our database.

        if self.email.data != current_user.email:
            patient_email = Patient.query.filter_by(self.email.data).first()
            psych_email = Psychiatrist.query.filter_by(self.email.data).first()

            if psych_email or patient_email:  # If there is an email associated, then raise a validation error.
                raise ValidationError('Error! Email is already in use!')

    def validate_password(self):
        # We don't want people accessing a logged in and making unauthorised changes to their account.
        # If hashed password from database does not match, raise validation error.
        if not check_password_hash(current_user.hashed_password, self.validate_password):
            raise ValidationError('Please enter the correct password.')

    def validate_delete_aware(self):

        # We don't want the user to accidentally make changes without being aware of them. Here, we can implement
        # logic for a checkbox.

        if not self.delete_aware:
            raise ValidationError('Please confirm your changes.')


# Form to delete accounts.

class DeleteAccountForm(AccountSettingFormBase):
    enter_password = PasswordField('Enter Password', [
        Length(min=8, max=35, message='Please enter a valid password.'),
        EqualTo('confirm_password', message='Both passwords must match'),
        DataRequired(message='Please enter a password.')])

    confirm_password = PasswordField('Confirm Password', [
        DataRequired(message='Please confirm your password.')])

    delete_aware = BooleanField('Confirm Changes')

    submit = SubmitField('Update')


# Form to update user settings.

class UpdateUserAccountForm(AccountSettingFormBase):
    email = StringField('Email Address', [
        Length(min=2, max=100, message='Please enter a valid email address.'),
        Email(message='Invalid email address.'),
        DataRequired(message='Please enter an email address.')])

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

    # We don't need to write two different forms, just make an if statement.

    bio = None

    if current_user.user_authentication == "Patient":

        bio = StringField('Medical Conditions', [
            Length(max=500, message='There is a maximum of 500 characters for this field.')
        ])

    elif current_user.user_authentication == "Psychiatrist":

        bio = StringField('Psychiatrist Bio', [
            Length(max=500, message='There is a maximum of 500 characters for this field.')
        ])

    # Confirm Changes -----------------------------------------------------------

    validate_password = PasswordField('Validate Password', [
        Length(min=8, max=35, message='Please enter a valid password.'),
        DataRequired(message='Please enter a password.')])

    delete_aware = BooleanField('Confirm Changes')

    submit = SubmitField('Update')
