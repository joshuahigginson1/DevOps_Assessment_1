# Blueprint Task: Stores all routes related to our 'main_layout' web page.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

from flask import Blueprint, url_for, flash, redirect, render_template
from flask_login import current_user, login_user
from flaskr.register.models import Psychiatrist, Patient  # Imports our Psychiatrist and Patient Models

from flaskr.auth.forms import LoginForm  # Imports our Login Form.

from flask_argon2 import check_password_hash  # Imports Argon2 to check password hash against our database.

# Blueprint Configuration -----------------------------------------------------------------

main_bp = Blueprint(
    'main_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------
@main_bp.route('/', methods=['GET', 'POST'])
def homepage():
    if current_user.is_authenticated:  # If user is already logged in, take them immediately to their dashboard.
        flash('You are already signed in!', 'primary')  # Displays message to user.
        return redirect(url_for('dashboard_bp.dashboard'))

    login_form = LoginForm()  # Initialise login form.

    if login_form.validate_on_submit():  # If the login form is valid, then...

        # Search for an account in both the patient and psychiatrist tables, within our SQL database.

        patient_account_check = Patient.query.filter_by(email=login_form.email.data).first()
        psych_account_check = Psychiatrist.query.filter_by(email=login_form.email.data).first()

        # If there is a patient account, and the two hashed passwords match, then execute the following code:

        if patient_account_check and check_password_hash(patient_account_check.hashed_password, login_form.password.data):

            login_user(patient_account_check, remember=login_form.remember.data)
            flash('Signed in successfully!', 'success')  # Displays message to user.
            return redirect(url_for('dashboard_bp.dashboard'))

            # Next iteration of sprint, we need to redirect the patient to a greetings page, where they fill out mood.

        # Else if there is a psychiatrist account, and the two hashed passwords match, then execute the following code:

        elif psych_account_check and check_password_hash(psych_account_check.hashed_password, login_form.password.data):

            login_user(psych_account_check, remember=login_form.remember.data)
            flash('Signed in successfully!', 'success')  # Displays message to user.
            return redirect(url_for('dashboard_bp.dashboard'))

        else:
            flash('Please check your login details and try again.', 'warning')  # Flashes a warning on screen.
            return redirect(url_for('main_bp.homepage'))

    return render_template(
        'main/homepage.html',
        title='Homepage ~ MiWell',
        login_form=login_form
    )


@main_bp.route('/about', methods=['GET'])
def about():
    return render_template('main/about.html', title='About ~ MiWell')