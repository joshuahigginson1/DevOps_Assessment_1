"""
Creates the Schema used to store our app's user information.
"""

# Imports --------------------------------------------------------------------------------

from flaskr import db  # import our database instance, stored as 'variable' in our __init__.py file.


# Classes --------------------------------------------------------------------------------


class PatientFeelings(db.Model):  # Represents how the user is feeling on a fixed scale.
    __tablename__ = 'patient_feelings'
    feelings_id = db.Column(db.Integer, primary_key=True)
    date_id = db.Column(db.Date)
    current_feeling = db.Column(db.String(30), nullable=False)  # How the patient feels today.
    feeling_comparison = db.Column(db.String(8), nullable=False)  # Better or worse than yesterday.
    patient_comment = db.Column(db.String(200))
    psychiatrist_comment = db.Column(db.String(200))  # Psychs leave their comment in this section.
    date_patient_updated = db.Column(db.Date)
    date_psychiatrist_updated = db.Column(db.Date)

    # Relationships ------------------------------------------------------------------------

    behaviours = db.relationship("PatientBehaviours", back_populates="feeling")

    patient_id = db.Column(db.String(50), db.ForeignKey('patient.username'))  # The username of the assigned patient.
    patient = db.relationship('Patient', back_populates='feelings')


class PatientBehaviours(db.Model):  # How the user has behaved throughout the day, can log many behaviours per day.
    __tablename__ = 'patient_behaviours'
    behaviour_id = db.Column(db.Integer, primary_key=True)
    behaviour = db.Column(db.String(50))  # The actual behaviour.

    # Relationships ------------------------------------------------------------------------

    feelings_id = db.Column(db.Integer, db.ForeignKey('patient_feelings.feelings_id'))
    feeling = db.relationship("PatientFeelings", back_populates="behaviours")

    # Class Method Override ---------------------------------------------------------------

    def get_id(self):  # Returns the behaviour_id as our primary 'id'.
        return self.behaviour_id
