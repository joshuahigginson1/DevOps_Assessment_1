# This script manages the update and delete functionality.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, redirect, url_for, request, flash

from flask_login import current_user, login_required

from flaskr import db

from flaskr.acc_settings.forms import UpdateUserAccountForm, DeleteAccountForm

from flask_argon2 import generate_password_hash

# Blueprint Configuration -----------------------------------------------------------------
from flaskr.register.models import Patient, Psychiatrist

settings_bp = Blueprint(
    'settings_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Routes ----------------------------------------------------------------------------------
@settings_bp.route('/dashboard/account_settings', methods=['GET', 'POST'])
@login_required
def account_settings():
    update_form = UpdateUserAccountForm()  # Initialise our update user form.

    if request.method == 'GET':  # Loads data into field on HTTP get request.
        update_form.first_name.data = current_user.first_name
        update_form.last_name.data = current_user.last_name
        update_form.email.data = current_user.email
        update_form.postcode.data = current_user.postcode
        update_form.phone_number.data = current_user.phone_number

        if current_user.user_authentication == 'Patient':
            update_form.bio.label = 'Medical Conditions'
            update_form.bio.data = current_user.medical_conditions

        elif current_user.user_authentication == 'Psychiatrist':
            update_form.bio.label = 'Psychiatrist Bio'
            update_form.bio.data = current_user.psych_bio

    elif update_form.validate_on_submit():  # Link current user info to our update form.

        current_user.first_name = update_form.first_name.data
        current_user.last_name = update_form.last_name.data
        current_user.email = update_form.email.data
        current_user.phone_number = update_form.phone_number.data
        current_user.postcode = update_form.postcode.data

        if current_user.user_authentication == 'Patient':
            current_user.medical_conditions = update_form.bio.data

        elif current_user.user_authentication == 'Psychiatrist':
            current_user.psych_bio = update_form.bio.data

        db.session.commit()  # ... Adds the changes to our database.

        flash("You have successfully changed your settings!", "primary")
        return redirect(url_for('main_bp.homepage'))

    if current_user.user_authentication == "Patient":

        return render_template(
            'acc_settings/patient_settings.html',
            title='User Settings ~ MiWell',
            form=update_form
        )

    elif current_user.user_authentication == "Psychiatrist":
        return render_template(
            'acc_settings/psych_settings.html',
            title='Psychiatrist Settings ~ MiWell',
            form=update_form
        )


@settings_bp.route('/dashboard/acc_settings/acc_deletion', methods=['GET', 'POST'])
@login_required
def delete_account():
    delete_form = DeleteAccountForm()

    if delete_form.validate_on_submit():  # If delete form validation is successful...

        # Here, we query the database for the primary ID our user.

        if current_user.user_authentication == 'Patient':
            account = Patient.query.get(current_user.username)

        elif current_user.user_athentication == 'Psychiatrist':
            account = Psychiatrist.query.get(current_user.bacp_number)

        db.session.delete(account)
        db.session.commit()  # ... Deletes the user from our database.

        flash("Account Deleted. See you soon!", "danger")
        return redirect(url_for('main_bp.homepage'))

    return render_template(
        'acc_settings/delete_account.html',
        title='Delete Account ~ MiWell',
        form=delete_form
    )
