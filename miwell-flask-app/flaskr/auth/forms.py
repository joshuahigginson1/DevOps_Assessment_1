# Generates the forms for user registration.

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm  # Import our Flask Form.
from wtforms import StringField, PasswordField, SubmitField, BooleanField  # Import our field types.
from wtforms.validators import DataRequired, Email # Import our validators.

# Classes --------------------------------------------------------------------------------


class LoginForm(FlaskForm):
    email = StringField('Email', [DataRequired(), Email()])

    password = PasswordField('Password', DataRequired())

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')
