# Retrieve info from database.
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import PasswordField, BooleanField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email
from flask_argon2 import check_password_hash







class DeleteAccountForm(FlaskForm):





class UserSettingFormBase(FlaskForm):

    def validate_email(self, email, user_table):

        # here, we check to see that there are no duplicate emails within our database.

        if email.data != current_user.email:
            email = user_table.query.filter_by(email.email.data).first()

            if email:  # If there is an email associated, then raise a validation error.
                raise ValidationError('Error! Email is already in use!')

    def validate_password(self, password):

    # If hashed password from database does not match, raise validation error.
        if not check_password_hash(current_user.hashed_password, password):
            raise ValidationError('Please enter the correct password.')


    def check_delete_aware(self):

        if checkbox not True:
            raise ValidationError('Please confirm the changes.')




        pass


class UpdatePatientAccountForm(FlaskForm):

    first_name = StringField('First Name', [
        DataRequired(),
        Length


    ])

    last_name = StringField('Last Name', [






    ])

    email = StringField('Last Name', [

        Email







    ])

    # require_password

    validate_password(my_password)






    submit = SubmitField('Update')



# Read user settings.




# Require old password verification.





class UpdatePsychiatristAccountForm(FlaskForm):

    first_name = StringField('First Name', [
        DataRequired(),
        Length


    ])

    last_name =

    email =

    # require_password

    submit = SubmitField('Update')




