# This blueprint handles the registration of new users and new psychiatrists for the web app.

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

# from flask_login import login_user, current_user, logout_user, login_required

# Blueprint Configuration -----------------------------------------------------------------

register_bp = Blueprint(
    'register_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------
@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template(
        'register/register_page.html', title='Register ~ MiWell')