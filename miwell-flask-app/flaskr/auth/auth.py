# This blueprint stores all routes related to user authentication.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, url_for, flash, redirect, session
from flask_login import login_manager, logout_user
from flaskr.register.models import Psychiatrist, Patient

# Blueprint Configuration -----------------------------------------------------------------

auth_bp = Blueprint(
    'auth_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------


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
