# This script adds the functionality to generate new unique users into our database.

from flask_argon2 import generate_password_hash
import random
import string


def generate_random_bacp():  # Generates a valid random BACP number.
    bacp_number = str(random.randint(1000000000000000, 9999999999999999))
    return bacp_number


def generate_random_username():  # Generates a valid random username.
    letters = string.ascii_letters

    return ''.join(random.choice(letters) for i in range(10))


def generate_new_patient():  # Generates a valid new patient.

    new_patient = {
        'username': generate_random_username(),
        'hashed_password': generate_password_hash("TestPatient"),
        'email': "TestPatient@Test.com",
        'first_name': "Test",
        'last_name': "Patient",
        'phone_number':"11111111111",
        'postcode':"L1 6DQ",
        'medical_conditions': "I am a Test.",
        'user_authentication': "Patient"
    }

    return new_patient


def generate_new_psychiatrist():  # Generates a valid new patient.

    new_psychiatrist = {
        'bacp_number': generate_random_bacp(),
        'email': "TestPsychiatrist@Test.com",
        'hashed_password': generate_password_hash("TestPsychiatrist"),
        'first_name': "Test",
        'last_name': "Psychiatrist",
        'phone_number': "66666666666",
        'postcode': "NN6 7TL",
        'psychiatrist_bio': "I am a Test.",
        'user_authentication': "Psychiatrist"
    }

    return new_psychiatrist
