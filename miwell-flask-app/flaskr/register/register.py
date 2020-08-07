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

        else:

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

    return render_template(
        'register/psych_register_page.html',
        title='Register Psychiatrist ~ MiWell',
        psychiatrist_form=psychiatrist_form
    )
