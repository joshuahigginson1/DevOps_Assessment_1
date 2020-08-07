"""
This file is a template for creating and configuring a blueprint within Flask.

Blueprint Task: Write what the blueprint does HERE.
"""

# Imports --------------------------------------------------------------------------------

import datetime

from flask import Blueprint, render_template, redirect, url_for, flash

from flask_login import current_user, login_required

from flaskr import db
from flaskr.mood_tracker.forms import MoodForm

from flaskr.mood_tracker.models import PatientFeelings, PatientBehaviours

# Blueprint Configuration -----------------------------------------------------------------


mood_tracker_bp = Blueprint(
    'mood_tracker_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)

# Routes ----------------------------------------------------------------------------------

@mood_tracker_bp.route('/user_greeting', methods=['GET', 'POST'])
@login_required
def user_greeting():
    # Helper Methods -----------------------------------------

    def has_user_posted_today():

        date_now = datetime.datetime.utcnow().date()  # Get today's date.

        # Here, we look for any posts in patient feelings, that were submitted on today's date.

        any_posts_today = db.session.query(PatientFeelings).filter_by(date_submitted_utc=date_now).first()

        if any_posts_today:  # If the user has posted today, then we take them straight to the dashboard.
            flash('Greetings! Your mood has already been tracked for today!', 'primary')
            return redirect(url_for('dashboard_bp.dashboard'))

        else:  # Otherwise, ignore.
            pass

    # Forms --------------------------------------------------

    mood_form = MoodForm()  # Initialises a new instance of our Mood Form.

    # Execute Code -------------------------------------------

    has_user_posted_today()  # Check to see if user has posted today.

    if mood_form.validate_on_submit():  # If the mood form is successfully posted:

        current_date_utc = datetime.datetime.utcnow().date()  # Set once to avoid time conflict between two tables.

        new_feeling = PatientFeelings(
            patient_id=current_user.username,  # Patient ID equal to current user's username.
            current_feeling=mood_form.current_feeling.data,
            feeling_comparison=mood_form.feeling_comparison.data,
            date_submitted_utc=current_date_utc,  # Date equal to today's date.
            patient_comment=mood_form.patient_comment.data,
            psychiatrist_comment=None
        )

        db.session.add(new_feeling)  # Adds new feeling to feelings table.

        for behaviour in mood_form.behaviours:  # Adds a new database entry for each behaviour in our form.

            new_behaviour = PatientBehaviours(

                date_submitted_utc=current_date_utc,
                patient_id=current_user.username,  # Patient ID equal to current user's username.
                behaviour=behaviour
            )

            db.session.add(new_behaviour)

        db.session.commit()  # Commits the data to our database.

        flash('Your mood has been tracked for today. Thank you.', 'primary')
        return redirect(url_for('dashboard_bp.dashboard'))

    return render_template(
        'mood_tracker/user_greeting.html',
        title='Greetings! ~ MiWell',
        form=mood_form
    )
