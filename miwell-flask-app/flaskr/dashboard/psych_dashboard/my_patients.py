# Contains the code for managing psychatrist post comments.

# Imports --------------------------------------------------------------------------------

from datetime import datetime

from flask_login import current_user

from flaskr.mood_tracker.forms import MoodReview

from flaskr import db
from flaskr.mood_tracker.models import PatientFeelings

from flaskr.register.models import Patient


# Functions ------------------------------------------------------------------------------

def get_my_patients():  # Here, we get all the patients assigned to a user.
    my_patients = db.session.query(Patient).filter_by(psychiatrist_id=current_user.bacp_number).all()

    return my_patients


def get_my_flagged():  # Here, we get all the flagged patients assigned to a user.
    my_flagged_patients_query = db.session.query(Patient).filter_by(psychiatrist_id=current_user.bacp_number).filter_by(requires_urgent_help=True).all()

    return my_flagged_patients_query


def get_my_moods():  # Get all moods.
    my_patients = get_my_patients()
    my_patient_moods = db.session.query(Patient).filter_by(psychiatrist_id=current_user.bacp_number).filter_by(patient_id=my_patients.username).all()

    return my_patient_moods


def get_my_flagged_moods():  # Get all flagged moods.
    flagged_patients = get_my_flagged()
    flagged_moods = db.session.query(PatientFeelings).filter_by(patient_id=flagged_patients.username).all()

    return flagged_moods


def get_moods_not_replied():  # Get all moods not replied to.
    my_patients = get_my_patients()
    moods_not_replied = db.session.query(Patient).filter_by(psychiatrist_id=current_user.bacp_number).filter_by(requires_urgent_help=True).filter_by(patient_id=my_patients.username).filter_by(PatientFeelings.date_psychiatrist_updated is None).all()

    return moods_not_replied


# Here, we get all posts for a specific user.
def get_patient_mood(patient_id, limit):
    patient_mood = db.session.query(PatientFeelings).filter_by(PatientFeelings.patient_id == patient_id).limit(limit).all()

    return patient_mood


def get_patient_mood_by_date(patient, limit, date):
    patient_mood = get_patient_mood(patient, limit)
    mood_by_date = patient_mood.filter_by(PatientFeelings.date_id == date).all()

    return mood_by_date


# Methods --------------------------------------------------------------------------------


def psychiatrist_comment(post_id):
    # Forms --------------------------------------------------

    psychiatrist_mood_review = MoodReview()  # Initialises a new instance of our Mood Review Form.

    # Functions ----------------------------------------------

    if psychiatrist_mood_review.validate_on_submit():
        # Queries ----------------------------------------------

        # Find the corresponding post ID from our table, and store the values.
        update_field = db.PatientFeelings.query.filter_by(feelings_id=post_id).first()

        # Get the user ID corresponding to this post.

        patient_id = update_field.username

        # Find the corresponding user, and set their 'in danger' box to safe.
        update_safety = db.Patient.query.filter_by(username=patient_id).first

        update_field.psychiatrist_comment = psychiatrist_mood_review.psychiatrist_comment
        update_field.date_psychiatrist_updated = datetime.datetime.utcnow().date()
        update_safety.requires_urgent_help = False

        db.session.commit()
