# This blueprint stores all routes related to user authentication.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, url_for, flash, redirect
from flask_login import login_manager

# Blueprint Configuration -----------------------------------------------------------------

auth_bp = Blueprint(
    'auth_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------


@login_manager.user_loader  # Checks to see if a user is logged in, every time a page is loaded.
def load_user(user_id):
  if session['account_type'] == 'Admin':
      return Admin.query.get(int(user_id))
  elif session['account_type'] == 'Merchant':
      return Merchant.query.get(int(user_id))
  else:
      return None


@login_manager.unauthorized_handler  # Redirects unauthorised users back to the homepage.
def unauthorised():
    flash('You must be logged in to view that page.')
    return redirect(url_for('main_bp.homepage'))
