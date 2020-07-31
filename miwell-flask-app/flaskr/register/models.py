# Creates the Schema used to store our app's user information.

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.
from flask_login import UserMixin  # Provides useful methods for managing the users or our app.


# Classes --------------------------------------------------------------------------------

class CommonUser(db.Model):

    __abstract__ = True  # An abstract class states that this class should NOT be mapped to a table within our database.

    email = db.Column(db.String(50), nullable=False)
    hashed_password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    postcode = db.Column(db.String(10), nullable=False)
    user_authentication = db.Column(db.String(20), nullable=False)


class Patient(UserMixin, CommonUser):  # Creates the schema for a 'User table' within our database.

    __tablename__ = 'registered_patients'  # Sets SQL database table name.

    username = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    medical_conditions = db.Column(db.String(500))


class Psychiatrist(UserMixin, CommonUser):
    __tablename__ = 'registered_psychiatrists'

    bacp_number = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    psychiatrist_bio = db.Column(db.String(500))
