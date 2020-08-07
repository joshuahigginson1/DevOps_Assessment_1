"""
Creates the Schema used to store our app's user information.
"""

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.
from flask_login import UserMixin  # Provides useful methods for managing the users or our app.


# Classes --------------------------------------------------------------------------------

class PatientMood(db.Model):  # Creates the schema for a 'Mood Table' within our database.
    __tablename__ = 'mood_table'
    id = db.Column(db.Integer, primary_key=True)  # Auto Increment an id.
    patient_id = db.Column(db.ForeignKey())


    def __repr__(self):  # Define the self representation of our data.
        return ''.join(['UserID: ', str(self.id), '\r\n', 'Email: ', self.email])
