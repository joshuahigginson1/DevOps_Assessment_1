# tests/front_end_tests.py

import unittest
import urllib3

from flask_testing import LiveServerTexstCase
from selenium import webdriver

from flaskr import initialise_app, db
from flaskr.register.models import Patient, Psychiatrist

from flask_argon2 import generate_password_hash  # For generating password hashes.


class TestBase(LiveServerTestCase):

    def create_app(self):
        config_name = 'testing'
        app = initialise_app(config_name)
        app.config.update(
            SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:W33Y15nITj*I&k97@localhost:3306/miwell_test_database",
            LIVESERVER_PORT=8943  # Change the port that the liveserver listens on.
        )
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Safari()
        self.driver.get(self.get_server_url())

        db.session.commit()  # Commits anything that is currently left in our session stage to the database.
        db.drop_all()  # Drops the database schema.
        db.create_all()  # Creates our database schema.

        test_patient = Patient(  # Create a test patient.
            username='test_patient',
            hashed_password=generate_password_hash("test_patient"),
            email='test_patient@patient.com',
            first_name='Test',
            last_name='Patient',
            phone_number='01234567891',
            postcode='CV21 M12',
            medical_conditions='I am a test patient with no medical conditions.',
            user_authentication="Patient")

        test_psychiatrist = Psychiatrist(  # Create a test psychiatrist.
            bacp_number='1234567812345678',
            hashed_password=generate_password_hash("test_psychiatrist"),
            email='test_psychiatrist@psychiatrist.com',
            first_name='Test',
            last_name='Psychiatrist',
            phone_number='10987654321',
            postcode='NN6 7TL',
            psychiatrist_bio='I am a test psychiatrist with no real psychiatric knowledge.',
            user_authentication="Psychiatrist")

        db.session.add(test_patient)
        db.session.add(test_psychiatrist)
        db.session.commit()  # Saves our new users to the database.

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urllib3.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    unittest.main()
