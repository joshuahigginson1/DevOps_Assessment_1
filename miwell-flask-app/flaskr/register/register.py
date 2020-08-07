# This blueprint handles the registration of new users and new psychiatrists for the web app.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, redirect, url_for, flash

from flaskr import db

from flaskr.register.forms import PatientRegistrationForm, PsychRegistrationForm
from flaskr.register.models import Patient, Psychiatrist

from flaskr.register.assign_patient_to_psychiatrist import psychiatrist_assign_function

from flask_argon2 import generate_password_hash

from flask_login import current_user


# Blueprint Configuration -----------------------------------------------------------------


register_bp = Blueprint(
    'register_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__
)


# Routes ----------------------------------------------------------------------------------
@register_bp.route('/register', methods=['GET', 'POST'])
def register_patient():
    if current_user.is_authenticated:  # If current user is already logged in, direct them to dashboard.
        flash('You are already signed in!', 'primary')  # Displays message to user.
        return redirect(url_for('main_bp.homepage'))

    patient_form = PatientRegistrationForm()

    if patient_form.validate_on_submit():  # If the submitted form passes validation, then...

        available_psychiatrist = psychiatrist_assign_function()  # Attempt to assign a psychiatrist to this patient.

        # if our query returns no psychiatrists, flash a danger alert to our user & take them back to the homepage.
        if available_psychiatrist is None:
            flash('Error! Could not currently register you with a psychiatrist. Please try again tomorrow.', 'danger')

            return redirect(url_for('main_bp.homepage'))

        # Search for any patients within the database that have an identical email or username.

        existing_psych_email = Psychiatrist.query.filter_by(email=patient_form.email.data).first()
        existing_patient_email = Patient.query.filter_by(email=patient_form.email.data).first()
        existing_patient_username = Patient.query.filter_by(username=patient_form.username.data).first()

        # If there are no accounts with a matching email or username, then execute the following code:

        if existing_patient_email is None and existing_patient_username is None and existing_psych_email is None:

            hashed_password = generate_password_hash(patient_form.password.data)  # Generate password hash with Argon2

            patient = Patient(
                username=patient_form.username.data,
                hashed_password=hashed_password,
                email=patient_form.email.data,
                first_name=patient_form.first_name.data,
                last_name=patient_form.last_name.data,
                phone_number=patient_form.phone_number.data,
                postcode=patient_form.postcode.data,
                medical_conditions=patient_form.medical_conditions.data,
                user_authentication="Patient",
                psychiatrist_id=available_psychiatrist  # Back-Ref.
            )  # Translates WTForm data to a Patient object, ready for use with SQL-Alchemy.

            db.session.add(patient)  # Adds our new patient object to the MySQL database.
            db.session.commit()

            flash('Congratulations, you are now a registered user!', 'success')
            return redirect(url_for('main_bp.homepage'))

        elif existing_psych_email:  # If there is an existing psychiatrist email, then...
            flash('A psychiatrist has already registered with this email address.', 'danger')

        elif existing_patient_email:  # If there is an existing patient email, then...
            flash('An account already exists with the current email address.', 'danger')

        elif existing_patient_username:  # If there is an existing patient username, then...
            flash('A user already exists with your chosen username.', 'danger')

    return render_template(
        'register/patient_register_page.html',
        title='Register ~ MiWell',
        patient_form=patient_form
    )


@register_bp.route('/register_psychiatrist', methods=['GET', 'POST'])
def register_psychiatrist():
    if current_user.is_authenticated:  # If current user is already logged in, direct them to dashboard.
        flash('You are already signed in!', 'primary')  # Displays message to user.
        return redirect(url_for('main_bp.homepage'))

    psychiatrist_form = PsychRegistrationForm()

    if psychiatrist_form.validate_on_submit():  # If the submitted form passes validation, then...

        # Search for any psychiatrists within the database that have an identical email or BACP number.

        existing_psych_bacp = Psychiatrist.query.filter_by(bacp_number=psychiatrist_form.bacp_number.data).first()
        existing_psych_email = Psychiatrist.query.filter_by(email=psychiatrist_form.email.data).first()
        existing_patient_email = Patient.query.filter_by(email=psychiatrist_form.email.data).first()

        # If there are no accounts with a matching email or bacp number, then execute the following code:

        if existing_psych_email is None and existing_psych_bacp is None and existing_patient_email is None:

            hashed_password = generate_password_hash(psychiatrist_form.password.data)  # Generate password hash.

            psychiatrist = Psychiatrist(
                bacp_number=psychiatrist_form.bacp_number.data,
                hashed_password=hashed_password,
                email=psychiatrist_form.email.data,
                first_name=psychiatrist_form.first_name.data,
                last_name=psychiatrist_form.last_name.data,
                phone_number=psychiatrist_form.phone_number.data,
                postcode=psychiatrist_form.postcode.data,
                psychiatrist_bio=psychiatrist_form.psychiatrist_bio.data,
                user_authentication="Psychiatrist"
            )  # Translates WTForm data to a Psychiatrist SQL_Alchemy object.

            db.session.add(psychiatrist)  # Adds our new psychiatrist object to the MySQL database.
            db.session.commit()

            flash('Congratulations, you are now a registered psychiatrist!', 'success')
            return redirect(url_for('main_bp.homepage'))

        elif existing_patient_email:  # If there is an existing patient email, then...
            flash('An account already exists with the current email address.', 'danger')

        elif existing_psych_email:  # If there is an existing psychiatrist email, then...
            flash('A psychiatrist has already registered with this email address.', 'danger')

        elif existing_psych_bacp:  # If there is an existing psychiatrist with the same BACP number, then...
            flash('A psychiatrist has already registered with this BACP number.', 'danger')

    return render_template(
        'register/psych_register_page.html',
        title='Register Psychiatrist ~ MiWell',
        psychiatrist_form=psychiatrist_form
    )
