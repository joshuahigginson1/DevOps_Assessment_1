# This blueprint stores all routes related to user authentication.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, url_for, flash, redirect, session
from flask_login import login_manager, logout_user, current_user, login_user
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

def login():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.dashboard'))

    login_form = LoginForm()

    if login_form.validate_on_submit():

        user=Users.query.filter_by(email=login_form.email.data).first()

        if user and check_password_hash(user.password, login_form.password.data):

            login_user(user, remember=login_form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)

            else:
                flash('Please check your login details and try again.')
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', login_form=login_form)









@login_manager.user_loader  # Checks to see if a user is logged in, every time a page is loaded.
def load_user(id):
    if session['account_type'] == 'Psychiatrist':
        return Psychiatrist.query.get(int(id))

    elif session['account_type'] == 'Patient':
        return Patient.query.get(int(id))

    else:
        return None


@login_manager.unauthorized_handler  # Redirects unauthorised users back to the homepage.
def unauthorised():
    flash('You must be logged in to view that page.')
    return redirect(url_for('main_bp.homepage'))


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
