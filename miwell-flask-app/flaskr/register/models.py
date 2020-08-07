# Creates the Schema used to store our app's user information.

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our init_test_cases.py file.
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

class Psychiatrist(UserMixin, CommonUser):
    __tablename__ = 'psychiatrist_table'

    bacp_number = db.Column(db.String(16), primary_key=True, unique=True, nullable=False)
    psychiatrist_bio = db.Column(db.String(500))

    # One psychiatrist can have many patients. We model this with the function db.relationship.

    patients = db.relationship('Patient', backref='personal_psychiatrist')  # Models the one to many relationship.

    # Flask-Login Method Override ---------------------------------------------------------------

    def get_id(self):  # Returns the bacp_number as user ID in order to satisfy Flask-Login's requirements.
        return self.bacp_number

class Patient(UserMixin, CommonUser):  # Creates the schema for a 'User table' within our database.

    __tablename__ = 'patient_table'  # Sets SQL database table name.

    username = db.Column(db.String(50), primary_key=True, unique=True, nullable=False)
    medical_conditions = db.Column(db.String(500))

    # Models the fact that a patient can only ever have one psychiatrist.

    psychiatrist_id = db.Column(db.String(16), db.ForeignKey('psychiatrist_table.bacp_number'))

    # Flask-Login Method Override ---------------------------------------------------------------

    def get_id(self):  # Returns the username as user ID in order to satisfy Flask-Login's requirements.
        return self.username

