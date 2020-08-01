# This blueprint stores all functions and routes related to user authentication.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, url_for, flash, redirect
from flask_login import logout_user

from flaskr import login_manager

from flaskr.register.models import Psychiatrist, Patient  # Imports our Psychiatrist and Patient Models

# Blueprint Configuration -----------------------------------------------------------------


auth_bp = Blueprint(
    'auth_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------

@login_manager.unauthorized_handler  # Redirects unauthorised users back to the homepage.
def unauthorised():
    flash('You must be logged in to view that page.')
    return redirect(url_for('main_bp.homepage'))


@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main_bp.homepage'))


@login_manager.user_loader
def user_loader(user_id):
    user = Patient.query.get(user_id)
    if user is None:
        user = Psychiatrist.query.get(user_id)

        return user
