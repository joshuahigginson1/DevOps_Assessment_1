# This script contains the logic which pairs a patient to a psychiatrist upon registration.

# Imports -------------------------------------------------------------------------------------

from sqlalchemy import func

from flaskr import db
from flaskr.assign_patient_to_psychiatrist.models import PatientPsychiatristAssign

# Declare Variables ---------------------------------------------------------------------------

# Makes each variable easier to read within our SQLAlchemy queries.

psychiatrist_id = PatientPsychiatristAssign.psychiatrist_bacp_number
patient_id = PatientPsychiatristAssign.patient_username


# Define Function ------------------------------------------------------------------------------

def psychiatrist_assign_function():
    # We assign each patient a new psychiatrist upon registering an account.
    # A patient should not be able to register if no psychiatrists are registered in  system.

    count_psychiatrists = db.session.query(
        func.count(psychiatrist_id))  # Counts the number of psychiatrists in our table.

    print(str(count_psychiatrists))  # Outputs the raw SQL query to the terminal.

    #  SELECT COUNT(bacp_number) AS num_psychiatrists
    #  FROM psychiatrist_table;

    if count_psychiatrists == 0:

        chosen_psychiatrist = None

    else:  # We are free to assign the user a psychiatrist.
        # To prevent overworking psychiatrists, we assign our patient to  psychiatrist with the least # of patients.

        # The following query searches for the psychiatrist with the least number of patients assigned to them.

        chosen_psychiatrist = db.session.query(psychiatrist_id,
                                               func.count(patient_id)).group_by(psychiatrist_id).asc().limit(1)

        print(str(chosen_psychiatrist))  # Outputs the raw SQL query to our terminal.

        # FROM patient_psychiatrist_assignment_table
        # SELECT psychiatrist_bacp_number, COUNT(patient_username)
        # GROUP BY Psychiatrist.bacp_number DESC
        # LIMIT 1;

    return chosen_psychiatrist
