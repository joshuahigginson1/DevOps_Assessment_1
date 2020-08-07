"""
A template which lays out the basic syntax for a forms.py file using Flask and WTForms.
"""

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm, RecaptchaField  # Import our Flask Form.
from wtforms import StringField, SubmitField, RadioField, SelectField  # Import our field types.
from wtforms.validators import DataRequired, Length, Email  # Import our validators.


# Classes --------------------------------------------------------------------------------


class MoodForm(FlaskForm):  # Creates a child class called 'NewForm', inheriting from parent 'FlaskForm'.

    current_feeling = RadioField('How is your mental health today?',
                                 coerce=int,  # A tag to ensure that our validation works for RadioFields.
                                 choices=[(1, '1 - Excruciatingly bad.'),
                                          (2, '2 - '),
                                          (3, "3 - It's been better."),
                                          (4, '4 - '),
                                          (5, "5 - My mental health hasn't affected me today."),
                                          (6, '6 - '),
                                          (7, "7 - I'm feeling positive."),
                                          (8, '8 - '),
                                          (9, '9 - '),
                                          (10, '10 - On top of the world.')],

                                 validators=[DataRequired()])

    feeling_comparison = RadioField('How are you feeling compared to yesterday?',
                                    coerce=str,  # A tag to ensure that our validation works for RadioFields.
                                    choices=[('worse', 'Worse than yesterday.'),
                                             ('same', 'The same as yesterday.'),
                                             ('better', 'Better than yesterday.')],

                                    validators=[DataRequired()])

    behaviours = SelectField('Which behaviours have you experienced today?',
                             coerce=str,
                             choices=[('smiling', '😁 - Happy'),
                                      ('angry', '😡 - Angry.'),
                                      ('disappointed', '😞 - Disappointed.'),
                                      ('done_with_today', '😩 - Done with today.'),
                                      ('persevering', '😣 - Persevering.'),
                                      ('anxious', '😰 - Anxious.'),
                                      ('confused', '😕 - Confused.'),
                                      ('worried', '😟 - Worried.'),
                                      ('ill', '🤢 - Physically Ill'),
                                      ('exhausted', '🥵 - Exhausted'),
                                      ('accomplished', '🥳 - Accomplished'),
                                      ('star_struck', '🤩 - Star Struck'),
                                      ('scared', '😨 - Frightened')])

    patient_comment = StringField('Anything else bothering you today?', [
        Length(max=200, message='Please keep your message under 200 characters.')])

    submit = SubmitField('Complete Evaluation')

# Validator Syntax:
# VARIABLE = FIELD_TYPE('FIELD_NAME', [ # list of validators.
# VALIDATOR_TYPE(message=('ERROR_MESSAGE'),
# VALIDATOR_TYPE(message=('ERROR_MESSAGE')
# )])
