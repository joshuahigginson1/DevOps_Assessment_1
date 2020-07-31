"""
This file is a template for creating and configuring a blueprint within Flask.

Blueprint Task: Write what the blueprint does HERE.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

# from flask_login import login_user, current_user, logout_user, login_required

# Blueprint Configuration -----------------------------------------------------------------

mood_tracker_bp = Blueprint(
    'mood_tracker_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------
@mood_tracker_bp.route('/user_greeting', methods=['GET'])
def user_greeting():
    return render_template(
        'mood_tracker/user_greeting.html',
        title='~ Greetings! ~'
    )