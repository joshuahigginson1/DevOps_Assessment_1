# This script contains the logic which pairs a patient to a psychiatrist upon registration.

# Imports -------------------------------------------------------------------------------------
from os import abort

from sqlalchemy import func

from operator import itemgetter

from flaskr import db
from flaskr.register.models import Psychiatrist, Patient


# Define Function ------------------------------------------------------------------------------

def psychiatrist_assign_function():
    # We assign each patient a new psychiatrist upon registering an account.
    # A patient should not be able to register if no psychiatrists are registered in  system.

    count_psychiatrists = db.session.query(
        func.count(Psychiatrist.bacp_number))  # Counts the number of psychiatrists in our database.

    print('\n------------------------------------- START SQL RAW QUERY -------------------------------------\n')
    print(count_psychiatrists)  # Outputs the raw SQL query to the terminal.
    print('\n------------------------------------- END SQL RAW QUERY -------------------------------------\n')

    # Expected:
    # SELECT COUNT(patient_id)
    # FROM psychiatrist_table;

    count_patients = db.session.query(
        func.count(Patient.username))  # Counts the number of patients in our database.

    print('\n------------------------------------- START SQL RAW QUERY -------------------------------------\n')
    print(count_patients)  # Outputs the raw SQL query to the terminal.
    print('\n------------------------------------- END SQL RAW QUERY -------------------------------------\n')

    # Expected:
    # SELECT COUNT(psychiatrist_id)
    # FROM psychiatrist_table;

    (number_of_psychiatrists,) = count_psychiatrists.one()  # Here, we unpack the tuple which our query returns.
    print(f"The number of psychiatrists is: {number_of_psychiatrists}")

    (number_of_patients,) = count_patients.one()
    print(f"The number of patients is: {number_of_patients}")

    if number_of_psychiatrists == 0:  # We cannot assign a psychiatrist to a user, so we can't register them.

        print("\nThere are no psychiatrists currently in our table!\n")

        chosen_psychiatrist = None

    elif number_of_psychiatrists == 1 or number_of_patients == 0:

        # In this case, we just want to assign a value to the first available psychiatrist.

        (only_psychiatrist,) = db.session.query(Psychiatrist.bacp_number).first()

        print(f'\nThe only available psychiatrist is: {only_psychiatrist}')

        chosen_psychiatrist = only_psychiatrist  # We set the chosen psychiatrist as the only psychiatrist.

    else:
        # To prevent overworking psychiatrists, we assign our patient to the psychiatrist with the least # of patients.

        def find_least_busy_psychiatrist():
            # The following query searches for the psychiatrist with the least number of patients assigned to them.

            # First, we need to join our Psychiatrist and Patient tables together.

            # We reference everything as a property of Patient.
            psych_on_patients_join = db.session. \
                query(Psychiatrist.bacp_number, Patient.username). \
                outerjoin(Patient, Patient.psychiatrist_id == Psychiatrist.bacp_number)

            print('\n------------------------------------- START SQL RAW QUERY -------------------------------------\n')
            print(psych_on_patients_join)  # Outputs the raw SQL query to our terminal.
            print('\n------------------------------------- END SQL RAW QUERY -------------------------------------\n')

            # Expected:
            # SELECT psy.bacp_number, pat.username,
            # FROM psychiatrist psy
            # LEFT OUTER JOIN patient pat
            # ON psy.bacp_number=pat.psychiatrist_id;

            packed_psych_pat_qry = psych_on_patients_join.all()  # Return all search results as a list of tuples.

            print(f"The packed psych2patient query is:\n {packed_psych_pat_qry}\n")

            psych_to_patients_dict = dict()  # Initialise a new dictionary with our psychiatrist_id as keys.

            for packed_tuple in packed_psych_pat_qry:  # For every tuple in our search query:
                (psych_id, assigned_pat) = packed_tuple  # Here, unpack our tuple.

                if psych_to_patients_dict.get(psych_id) is None:  # If there is not currently a psych in our key...
                    psych_to_patients_dict[psych_id] = 0  # Create a new key, with a ' pat count' value of zero.

                if assigned_pat is None:  # If there is no patient assigned, then skip.
                    pass

                else:  # Otherwise, add one to dictionary count.
                    psych_to_patients_dict[psych_id] += 1

            print(f"Our psych2patient dictionary is: \n {psych_to_patients_dict}")

            lowest_psych_min = min(psych_to_patients_dict,  # Now, find the psychiatrist with the lowest key:value.
                                   key=psych_to_patients_dict.get)  # Use key to search by the key:value, NOT the key.

            return lowest_psych_min

        chosen_psychiatrist = find_least_busy_psychiatrist()

        print(f'\nThe psychiatrist with the least number of people assigned to them is: {chosen_psychiatrist}')

        print(f'\nThe chosen psychiatrist is: {chosen_psychiatrist}.\n')

    return chosen_psychiatrist
