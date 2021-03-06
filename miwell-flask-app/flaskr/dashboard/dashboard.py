# This blueprint handles configuration of the logged-in users' dashboard with correct information.

# Imports -------------------------------------------------------------------------------------------------

from flask import Blueprint, render_template

from flask_login import current_user, login_required

from flaskr.dashboard.psych_dashboard.my_patients import get_moods_not_replied, get_my_flagged_moods_and_accounts

from flaskr.error_handling.error_handling import error_page

# Blueprint Configuration --------------------------------------------------------------------------------


dashboard_bp = Blueprint(
    'dashboard_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Shared Routes ------------------------------------------------------------------------------------------

@dashboard_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    if current_user.user_authentication == 'Patient':

        return render_template(  # Returns our patient's personalised front end homepage.
            'dashboard/patient_dash/patient_dash.html',
            title=' Dashboard ~ MiWell',
            current_user=current_user
        )

    elif current_user.user_authentication == 'Psychiatrist':

        # We want to show only the flagged posts from users on the homepage.

        flagged_moods, accounts = get_my_flagged_moods_and_accounts()

        for account in accounts:
            print(account)

        # Use Jinja2 to render this info on screen.

        return render_template(  # Returns our patient's personalised front end homepage.
            'dashboard/psych_dash/psych_dash.html',
            title=' Dashboard ~ MiWell',
            current_user=current_user,
            flagged=flagged_moods,
            accounts=accounts
        )


# User Dashboard ---------------------------------------------------------------------------------------

@dashboard_bp.route('/dashboard/your_progress', methods=['GET'])
@login_required
def user_progress():
    if current_user.user_authentication == 'Psychiatrist':
        return error_page(404)

    elif current_user.user_authentication == 'Patient':

        return render_template(
            'dashboard/patient_dash/patient_progress.html',
            title=' Your Progress ~ MiWell',
            current_user=current_user
        )


@dashboard_bp.route('/dashboard/your_tools', methods=['GET'])
@login_required
def user_tools():
    if current_user.user_authentication == 'Psychiatrist':
        return error_page(404)

    elif current_user.user_authentication == 'Patient':

        return render_template(
            'dashboard/patient_dash/patient_tools.html',
            title=' Mindfulness Tools ~ MiWell',
            current_user=current_user
        )


# Psychiatrist Dashboard ------------------------------------------------------------------------------

@dashboard_bp.route('/dashboard/my_patients', methods=['GET'])
@login_required
def my_patients():
    if current_user.user_authentication == 'Patient':
        return error_page(404)

    elif current_user.user_authentication == 'Psychiatrist':
        pass






        return render_template(
            'dashboard/psych_dash/my_patients.html',
            title=' My Patients ~ MiWell',
            current_user=current_user
        )


@dashboard_bp.route('/dashboard/psychiatrist_tools', methods=['GET'])
@login_required
def psychiatrist_tools():
    if current_user.user_authentication == 'Patient':
        return error_page(404)

    elif current_user.user_authentication == 'Psychiatrist':
        pass

    return render_template(
        'dashboard/psych_dash/psychiatrist_tools.html',
        title=' psychiatrist Tools ~ MiWell',
        current_user=current_user
    )


@dashboard_bp.route('/dashboard/posts/<post_id>', methods=['GET', 'POST'])
@login_required
def post_review(post_id):

    # An outside generator will create the url.


    # According to the URL, we find the the post_id of our post in our table.


    # We render this form using Jinja2 template.
    # Our template will be different for users and psychiatrists, but essentially do the same thing.




    return render_template(
        'dashboard/psych_dash/psychiatrist_tools.html',
        title=' psychiatrist Tools ~ MiWell',
        current_user=current_user
    )