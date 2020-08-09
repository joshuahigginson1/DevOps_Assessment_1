# Contains the code for managing psychiatrist post comments.

# Imports --------------------------------------------------------------------------------

from datetime import datetime

from flask_login import current_user

from flaskr.mood_tracker.forms import MoodReview

from flaskr import db
from flaskr.mood_tracker.models import PatientFeelings

from flaskr.register.models import Patient


# Functions ------------------------------------------------------------------------------

def get_my_patients():  # Here, we get all the patients assigned to a user.

    my_patients_list = []

    my_patients_raw = db.session.query(Patient.username).filter_by(psychiatrist_id=current_user.bacp_number).all()
    # Returns usernames like this: [('joshua',), ('joshuahigginson12@gmail.com',), ('kriskringle',)]

    for raw_tuples in my_patients_raw:  # We need to unpack this tuple.
        (username,) = raw_tuples

        my_patients_list.append(username)  # Append each username to a list of patients.

    return my_patients_list  # Returns the list of patients.


def get_my_flagged():  # Here, we get all the flagged patients assigned to a user.

    my_flagged_list = []

    my_flagged_raw = db.session.query(Patient.username).filter_by(psychiatrist_id=current_user.bacp_number). \
        filter_by(requires_urgent_help=1).all()

    # Returns usernames like this: [('joshua',), ('joshuahigginson12@gmail.com',), ('kriskringle',)]

    for raw_tuples in my_flagged_raw:  # We need to unpack this tuple.
        (username,) = raw_tuples

        my_flagged_list.append(username)  # Append each username to a list of patients.

    return my_flagged_list


def get_my_moods():  # Get all moods.
    my_patients = get_my_patients()
    my_patient_moods = db.session.query(PatientFeelings).filter(Patient.username.in_(my_patients)).all()

    # Returns PatientFeelings objects, which can then be referenced later on in python with .feeling_id.

    return my_patient_moods


def get_my_flagged_moods_and_accounts():  # Get all flagged moods.
    flagged_patients = get_my_flagged()

    flagged_moods = db.session.query(PatientFeelings).filter(PatientFeelings.patient_id.in_(flagged_patients)).all()

    get_patient_info = []
    for moods in flagged_moods:
        patient = db.session.query(Patient).filter(Patient.username == moods.patient_id).all()

        # Python returns objects on their own, but in a list. We use index referencing to get it.

        get_patient_info.append(patient[0])

    # Returns PatientFeelings objects, which can then be referenced later on in python with .feeling_id.

    return flagged_moods, get_patient_info


def get_moods_not_replied():  # Get all moods not replied to.

    my_patients = get_my_patients()  # Returns all of the user's patients.

    list_of_moods = []

    for patient in my_patients:  # Returns all fields that have no comments in.
        patient_feelings_sorted = db.session.query(PatientFeelings).filter_by(patient_id=patient). \
            filter_by(psychiatrist_comment=None).all()

        for feelings in patient_feelings_sorted:  # Get rid of empty fields.
            if feelings:
                list_of_moods.append(patient_feelings_sorted)

    # Returns PatientFeelings objects, which can then be referenced later on in python with .feeling_id.

    return list_of_moods


def get_details_from_username(username):
    return db.session.query(Patient).filter_by(username=username)


"""
Didn't have enough time to fully implement this functionality.

def get_patient_mood(patient_id, limit):
    patient_mood = db.session.query(PatientFeelings).
        filter_by(PatientFeelings.patient_id == patient_id).limit(limit).all()

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
        update_field.date_psychiatrist_updated = datetime.utcnow().date()
        update_safety.requires_urgent_help = False

        db.session.commit()

        # Jinja Template must render form=psychiatrist_mood_review

"""