"""

Blueprint Task: Stores all routes related to user authentication under auth.py.
"""

# Imports --------------------------------------------------------------------------------

# Blueprint Configuration -----------------------------------------------------------------

auth_bp = Blueprint(
    'auth_bp',  # Name we want to assign to our Blueprint for Flask's internal routing purposes.
    __name__,
    template_folder='templates'
)

# Routes ----------------------------------------------------------------------------------
