# This script manages the update and delete functionality.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template, redirect, url_for, request, flash

from flask_login import current_user, login_required

from flaskr import db

from flaskr.acc_settings.forms import UpdateUserAccountForm, DeleteAccountForm

# Blueprint Configuration -----------------------------------------------------------------

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
@settings_bp.route('/dashboard/account_settings', methods=['GET', 'POST'])
@login_required
def account_settings():

    update_form = UpdateUserAccountForm()  # Initialise our update user form.

    if update_form.validate_on_submit():

        flash("Successfully altered your settings!", "secondary")
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

    return render_template(
        'acc_settings/patient_settings.html',
        title='User Settings ~ MiWell',
        form=delete_form
    )
