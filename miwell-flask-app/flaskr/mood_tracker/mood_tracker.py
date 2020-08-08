
# This blueprint stores the logic for our mood tracker functionality.

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
    static_folder='static')


# Logic -----------------------------------------------------------------------------------

# Routes ----------------------------------------------------------------------------------

@mood_tracker_bp.route('/user_greeting', methods=['GET', 'POST'])
@login_required
def user_greeting():

    # Forms --------------------------------------------------

    mood_form = MoodForm()  # Initialises a new instance of our Mood Form.

    # Execute Code -------------------------------------------

    # Check to see if user has posted today.

    date_right_now = datetime.datetime.utcnow().date()  # Get's today's date at the exact moment.

    # Here, we look for any posts in patient feelings, that were submitted on today's date.

    any_posts_today = db.session.query(PatientFeelings.patient_id).filter_by(date_id=date_right_now).first()

    if not any_posts_today:  # Otherwise, ignore.

        if mood_form.validate_on_submit():  # If the mood form is successfully posted:

            current_date_utc = datetime.datetime.utcnow().date() # Set once to avoid time conflict between two tables.

            new_feeling = PatientFeelings(
                patient_id=current_user.username,  # Patient ID equal to current user's username.
                current_feeling=mood_form.current_feeling.data,
                feeling_comparison=mood_form.feeling_comparison.data,
                date_id=current_date_utc,  # Date equal to today's date.
                patient_comment=mood_form.patient_comment.data,
                psychiatrist_comment=None
            )

            db.session.add(new_feeling)  # Adds new feeling to session.
            db.session.commit()  # Commits session to database.

            # Get the feeling ID of the current feeling, from the current patient.
            def get_feeling_id():
                # SELECT feelings_id
                # FROM patient_feelings
                # WHERE patient_id=current_user.username
                # AND date_id=current_date_utc
                # LIMIT 1

                query_feelings_id = db.session.query(PatientFeelings.feelings_id).\
                    filter_by(patient_id=current_user.username, date_id=current_date_utc)

                print('\n-------------------------------- START SQL RAW QUERY --------------------------------\n')
                print(query_feelings_id)  # Outputs the raw SQL query to our terminal.
                print('\n-------------------------------- END SQL RAW QUERY --------------------------------\n')

                (output_feeling_id, ) = query_feelings_id.first()  # Unpack tuple.

                return output_feeling_id

            for behaviour in mood_form.behaviours:  # Adds a new database entry for each behaviour in our form.

                new_behaviour = PatientBehaviours(
                    feelings_id=get_feeling_id(),
                    behaviour=behaviour.data
                )

                db.session.add(new_behaviour)
                db.session.commit()

            flash('Your mood has been tracked for today. Thank you.', 'primary')
            return redirect(url_for('dashboard_bp.dashboard'))

    elif any_posts_today:  # If the user has posted today, then we take them straight to the dashboard.
        flash('Greetings! Your mood has already been tracked for today!', 'primary')
        return redirect(url_for('dashboard_bp.dashboard'))

    return render_template(
        'mood_tracker/user_greeting.html',
        title='Greetings! ~ MiWell',
        form=mood_form
    )
