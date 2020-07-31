# This blueprint stores all routes related to user authentication.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, url_for, flash, redirect, session, render_template
from flask_login import logout_user, current_user, login_user

from flaskr import login_manager

from flaskr.register.models import Psychiatrist, Patient  # Imports our Psychiatrist and Patient Models

from flaskr.auth.forms import LoginForm  # Imports our Login Form.

from flask_argon2 import check_password_hash  # Imports Argon2 to check password hash against our database.

# Blueprint Configuration -----------------------------------------------------------------

auth_bp = Blueprint(
    'auth_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)

# Routes ----------------------------------------------------------------------------------

"""
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.dashboard'))

    login_form = LoginForm()  # Initialise login form.

    if login_form.validate_on_submit():  # If the login form is valid, then...

        # Search for an account in both the patient and psychiatrist tables, within our SQL database.

        patient_account_check = Patient.query.filter_by(email=login_form.email.data).first()
        psych_account_check = Psychiatrist.query.filter_by(email=login_form.email.data).first()

        # If there is a patient account, and the two hashed passwords match, then execute the following code:

        if patient_account_check and check_password_hash(patient_account_check.password, login_form.password.data):

            login_user(patient_account_check, remember=login_form.remember.data)
            return redirect(url_for('dashboard_bp.dashboard'))

            # Next iteration of sprint, we need to redirect the patient to a greetings page, where they fill out mood.

        # Else if there is a psychiatrist account, and the two hashed passwords match, then execute the following code:

        elif psych_account_check and check_password_hash(psych_account_check.password, login_form.password.data):

            login_user(psych_account_check, remember=login_form.remember.data)
            return redirect(url_for('dashboard_bp.dashboard'))

        else:
            flash('Please check your login details and try again.')
            return redirect(url_for('main_bp.homepage'))

    return render_template('login.html', title='Login', login_form=login_form)
"""


@login_manager.unauthorized_handler  # Redirects unauthorised users back to the homepage.
def unauthorised():
    flash('You must be logged in to view that page.')
    return redirect(url_for('main_bp.homepage'))


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main_bp.homepage'))

@ login_manager.user_loader
def user_loader(user_id):

    if user_id is not None:

        if current_user.user_authentication == "Psychiatrist":
            Psychiatrist.get(user_id)

        elif current_user.user_authentication == "Patient":
            Patient.get(user_id)

        else:
            return None

