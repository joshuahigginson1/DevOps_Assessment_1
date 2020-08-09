# This is a script dedicated to the read functionality of my mood tracker application.

# Imports -------------------------------------------------------------------------------

from flask_login import current_user

from flaskr.register.models import Psychiatrist

import db


# Functions

# A module to return the name of our psychiatrist.

# Modules ------------------------------------------------------------------------------


def get_psychiatrist_name():
    psych_name = db.session.query(Psychiatrist.first_name, Psychiatrist.last_name). \
        filter_by(bacp_number=current_user.psychiatrist_id)

    return psych_name


# A function to query our database, and return the last 14 days of posts.
"""
def return_user_posts(days_to_view):

# On the homepage for example, we could show only the most recent day to view.



    for posts in returned_table:

        # First, we need to query our database.

        # Select Date,


    def has_psychiatrist_made_comment():

        # Query our database, or currently existing fields. Either one.

        if:
            pass

        else:
            # Display the psychatrist comment.

"""
