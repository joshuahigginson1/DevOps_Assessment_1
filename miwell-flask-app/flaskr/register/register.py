# This blueprint handles the registration of new users and new psychiatrists for the web app.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, redirect, url_for, flash, current_app as app

from flaskr import db

from flaskr.register.forms import PatientRegistrationForm, PsychRegistrationForm
from flaskr.register.models import Patient, Psychiatrist

from flask_argon2 import generate_password_hash

from flask_login import login_user, current_user, logout_user, login_required

# Blueprint Configuration -----------------------------------------------------------------


register_bp = Blueprint(
    'register_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------
@register_bp.route('/register', methods=['GET', 'POST'])
def register_patient():

    if current_user.is_authenticated:  # If current user is already logged in, direct them to dashboard.
        return redirect(url_for('main_bp.homepage'))

    patient_form = PatientRegistrationForm()

    if form.validate_on_submit():

        hashed_password = generate_password_hash(patient_form.password.data)  # Generate password hash with Argon2

        patient = Patient(
            username=patient_form.username.data,
            hashed_password=hashed_password,
            email=patient_form.email.data,
            first_name=patient_form.first_name.data,
            last_name=patient_form.last_name.data,
            phone_number=patient_form.phone_number.data,
            postcode=patient_form.postcode.data,
            medical_conditions=patient_form.medical_conditions.data
        )  # Translates WTForm data to a Patient object, ready for use with SQL-Alchemy.

        db.session.add(patient)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_bp.homepage'))

    return render_template(
        'register/patient_register_page.html', title='Register ~ MiWell')


@register_bp.route('/register_psychiatrist', methods=['GET', 'POST'])
def register_psychiatrist():

    if current_user.is_authenticated:  # If current user is already logged in, direct them to dashboard.
        return redirect(url_for('main_bp.homepage'))

    form = PsychRegistrationForm()

    if form.validate_on_submit():

        hashed_password = generate_password_hash(form.password.data)  # Generate password hash with Argon2

        patient = Psychiatrist(
            username=form.username.data,
            hashed_password=hashed_password,
            email=form.email.data,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            phone_number=form.phone_number.data,
            postcode=form.postcode.data,
            medical_conditions=form.medical_conditions.data
        )  # Translates WTForm data to a Psychiatrist SQL_Alchemy object.

        db.session.add(patient)
        db.session.commit()

        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('main_bp.homepage'))

    return render_template(
        'register/psych_register_page.html', title='Register Psychiatrist ~ MiWell')