"""
This file is a template for creating and configuring a blueprint within Flask.

Blueprint Task: Write what the blueprint does HERE.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template

from flask_login import login_user, current_user, logout_user, login_required

from flaskr.mood_tracker.forms import MoodForm

# Blueprint Configuration -----------------------------------------------------------------

mood_tracker_bp = Blueprint(
    'mood_tracker_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)





# Forms -----------------------------------------------------------------------------------

# Routes ----------------------------------------------------------------------------------
@mood_tracker_bp.route('/user_greeting', methods=['GET', 'POST'])
def user_greeting():



    mood_form = MoodForm()

    if mood_form.validate_on_submit():
        mood_form =







    return render_template(
        'mood_tracker/user_greeting.html',
        title='Greetings! ~ MiWell',
        form=mood_form
    )
