"""
Blueprint Task: Stores all routes related to our 'main_layout' web page.
"""

# Imports --------------------------------------------------------------------------------

from flask import Blueprint, render_template
from flask import current_app as app

# Blueprint Configuration -----------------------------------------------------------------

main_bp = Blueprint(
    'main_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)


# Routes ----------------------------------------------------------------------------------
@main_bp.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('main/homepage.html', title='Homepage ~ MiWell')


@main_bp.route('/about', methods=['GET'])
def about():
    return render_template('main/about.html', title='About ~ MiWell')