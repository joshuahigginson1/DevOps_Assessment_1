# Creates the Schema used to store our app's user information.

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.
from flask_login import UserMixin  # Provides useful methods for managing the users or our app.


# Parent Class --------------------------------------------------------------------------------

class CommonUser(db.Model):
    __abstract__ = True  # An abstract class states that this class should NOT be mapped to a table within our database.

    email = db.Column(db.String(50), unique=True, nullable=False)
    hashed_password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    user_authentication = db.Column(db.String(20), nullable=False)


# Child Classes -----------------------------------------------------------------------------


class Patient(UserMixin, CommonUser):  # Creates the schema for a 'User table' within our database.

    __tablename__ = 'registered_patients'  # Sets SQL database table name.

    username = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    medical_conditions = db.Column(db.String(500))

    # Flask-Login Method Override ---------------------------------------------------------------

    def get_id(self):  # Returns the username as user ID in order to satisfy Flask-Login's requirements.
        return self.username


class Psychiatrist(UserMixin, CommonUser):
    __tablename__ = 'registered_psychiatrists'

    bacp_number = db.Column(db.String(20), primary_key=True, unique=True, nullable=False)
    psychiatrist_bio = db.Column(db.String(500))

    # Flask-Login Method Override ---------------------------------------------------------------

    def get_id(self):  # Returns the bacp_number as user ID in order to satisfy Flask-Login's requirements.
        return self.bacp_number
