# Creates the Schema used to store our the relationship between psychiatrists and patients.

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.
from flaskr.register.models import Patient, Psychiatrist


# Classes --------------------------------------------------------------------------------

class PatientPsychiatristAssign(db.Model):  # Creates the schema for a 'trans-table' within our database.

    __tablename__ = 'patient_psychiatrist_assignment_table'
    patient_username = db.Column(db.String(50), db.ForeignKey(Patient.username), primary_key=True, unique=True, nullable=False)
    psychiatrist_bacp_number = db.Column(db.String(20), db.ForeignKey(Psychiatrist.bacp_number), nullable=False)

    def __repr__(self):  # Defines the self representation of our data.
        return f'The user {self.patient_username} is assigned to psychiatrist: {self.psychiatrist_bacp_number}.'

"""    # Flask-Login Method Override ---------------------------------------------------------------

    def get_id(self):  # Overrides the patient's username as our Primary ID with Flask-Login. Probably not necessary.
        return self.patient_username"""
