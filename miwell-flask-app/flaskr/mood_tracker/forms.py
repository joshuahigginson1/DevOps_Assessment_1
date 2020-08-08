# A script which contains the mood tracker form and associated code.

# Imports --------------------------------------------------------------------------------

from flask_wtf import FlaskForm  # Import our Flask Form.
from wtforms import SubmitField, RadioField, TextAreaField, SelectMultipleField, widgets  # Import our field types.
from wtforms.validators import DataRequired, Length  # Import our validators.


# Custom Widgets ---------------------------------------------------------------------------

class MultiCheckboxField(SelectMultipleField):
    # A multiple-select, except displays a list of checkboxes.
    # Iterating the field will produce subfields and allows custom rendering of the enclosed checkbox fields.

    # Credit to Nick Timkovich -> github.com/nicktimko

    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# Classes --------------------------------------------------------------------------------


class MoodForm(FlaskForm):  # For patients to enter their mood within the system.

    current_feeling = RadioField(description='How is your mental health today?',
                                 coerce=int,  # A tag to ensure that our validation works for RadioFields.
                                 choices=[(1, 'Excruciatingly bad.'),
                                          (2, '2'),
                                          (3, "It's been better."),
                                          (4, '4'),
                                          (5, "My mental health hasn't affected me today."),
                                          (6, '6'),
                                          (7, "I'm feeling really positive."),
                                          (8, '8'),
                                          (9, '9'),
                                          (10, 'On top of the world.')],

                                 validators=[DataRequired()])

    feeling_comparison = RadioField(description='How are you feeling compared to yesterday?',
                                    coerce=str,  # A tag to ensure that our validation works for RadioFields.
                                    choices=[('worse', 'Worse than yesterday.'),
                                             ('same', 'The same as yesterday.'),
                                             ('better', 'Better than yesterday.')],

                                    validators=[DataRequired()])

    behaviours = MultiCheckboxField(description='Which behaviours have you experienced today?',
                                    coerce=str,
                                    choices=[('smiling', '😁 - Happy'),
                                             ('angry', '😡 - Angry'),
                                             ('disappointed', '😞 - Disappointed'),
                                             ('done_with_today', '😩 - Done with today'),
                                             ('persevering', '😣 - Persevering'),
                                             ('anxious', '😰 - Anxious'),
                                             ('confused', '😕 - Confused'),
                                             ('worried', '😟 - Worried'),
                                             ('ill', '🤢 - Physically ill'),
                                             ('exhausted', '🥵 - Exhausted'),
                                             ('accomplished', '🥳 - Accomplished'),
                                             ('star_struck', '🤩 - Star Struck'),
                                             ('scared', '😨 - Frightened')])

    patient_comment = TextAreaField('Anything else bothering you today?', [
        Length(max=200, message='Please keep your message under 200 characters.')])

    submit = SubmitField('Complete Evaluation')


class MoodReview(FlaskForm):

    psychiatrist_comment = TextAreaField('Your Comment:', [
        Length(max=200, message='Please keep your message under 200 characters.')])

    submit = SubmitField('Submit Review.')
