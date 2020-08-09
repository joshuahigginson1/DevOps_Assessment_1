"""
This file is a template for creating and configuring a blueprint within Flask.

This blueprint stores the code for displaying user and psych acc_settings, and editing an account.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import current_app as app

# from flask_login import login_user, current_user, logout_user, login_required

# Blueprint Configuration -----------------------------------------------------------------
from flask_login import current_user, login_required

from flaskr import db
from flaskr.acc_settings.forms import UpdatePatientAccountForm, UpdatePsychiatristAccountForm

settings_bp = Blueprint(
    'settings_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


def update_functionality(form):
    # When our user first sends their first 'get' request, we to pre-populate their form with existing data.

    if request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email

        if current_user.user_authentication == 'Patient':
            form.bio.data = current_user.medical_conditions

        elif current_user.user_authentication == 'Psychiatrist':
            form.bio.data = current_user.psych_bio

    elif patient_update_form.validate_on_submit():  # If form successfully validates...
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data

        if current_user.user_authentication == 'Patient':
            current_user.medical_conditions = form.bio.data

        elif current_user.user_authentication == 'Psychiatrist':
            current_user.psych_bio = form.bio.data

        db.session.commit()  # ... Adds the changes to our database.




# Routes ----------------------------------------------------------------------------------
@settings_bp.route('/dashboard/acc_settings', methods=['GET', 'POST'])
@login_required
def patient_acc_settings():

    patient_update_form = UpdatePatientAccountForm()  # Initialise our update patient form.

    update_functionality(patient_update_form)
        flash("Successfully altered your settings!", "secondary")
        return redirect(url_for('homepage_bp.homepage'))


    )



    return render_template(
        'dashboard/patient_dash/acc_settings.html',
        title='Settings ~ MiWell'
    )













@settings_bp.route('/dashboard/acc_settings', methods=['GET'])
# @login_required


def psychiatrist_acc_settings():

    psychiatrist_update_form = UpdatePsychiatristAccountForm()  # Initialise our update patient form.

    update_functionality(psychiatrist_update_form)

    return render_template(
        'dashboard/patient_dash/acc_settings.html',
        title='Settings ~ MiWell'
    )