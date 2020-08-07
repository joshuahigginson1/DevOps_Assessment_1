"""
This file is a template for creating and configuring a blueprint within Flask.

This blueprint stores the code for displaying user and psych acc_settings, and editing an account.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

# from flask_login import login_user, current_user, logout_user, login_required

# Blueprint Configuration -----------------------------------------------------------------

settings_bp = Blueprint(
    'settings_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates',
    static_folder='static'
)


# Routes ----------------------------------------------------------------------------------
@settings_bp.route('/dashboard/acc_settings', methods=['GET'])
# @login_required
def patient_acc_settings():
    return render_template(
        'dashboard/patient_dash/acc_settings.html',
        title='Settings ~ MiWell'
    )


@settings_bp.route('/dashboard/acc_settings', methods=['GET'])
# @login_required
def psychiatrist_acc_settings():
    return render_template(
        'dashboard/patient_dash/acc_settings.html',
        title='Settings ~ MiWell'
    )