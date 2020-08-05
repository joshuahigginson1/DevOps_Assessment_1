from flask import url_for
from selenium import webdriver
import unittest

from urllib3 import response

from flaskr import create_app, db
import threading
import time


# The setUpClass() method creates a Selenium client, which is stored in the client class variable.
# We then create an application context and a database.
# Then a real Flask server is started in a background thread.
# You can't use the Flask test client for this type of test.
# This is because the browser controlled by Selenium needs a real server it can connect to.
# The tearDownClass() just destroys all the resources created in setUpClass().
# The setUp() method checks that a client instance exists.
# if it doesn't, it tells the unit testing framework that the test needs to be skipped.
# This can happen if, for example, you did not have Firefox installed.


class LiveServerTestCase(unittest.TestCase):
    client = None

    @classmethod  # at the very start of the
    def setUpClass(cls):

        try:
            cls.client = webdriver.Safari()

        except:
            pass

        if cls.client:  # Only execute these tests if our web driver connects to a browser.

            cls.test_app = create_app('testing')  # Create our app within the app factory, using 'testing' config.

            # Here, we configure our application context and our request context.

            cls.app_context = cls.test_app.app_context()  # Creates an app context.
            cls.request_context = cls.test_app.test_request_context()

            cls.app_context.push()
            cls.request_context.push()

            # Anything between the app_context.push() and the app_context.pop() method will be considered to run...
            # ...within a 'app_context()' with statement.

            db.create_all()  # Creates our database.

            cls.server_thread = threading.Thread(target=cls.test_app.run)  # Configures our app to run in a new thread.
            cls.server_thread.start()  # Runs our app on a new thread.

            time.sleep(3)  # Give the server a second to ensure it is up, before running any tests prematurely.

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # Stop our flask server, and close our browser.

            cls.client.get(url_for('error_handling_bp.server_s'))
            cls.client.quit()  # .quit() is used to exit the browser, end the session, tabs, pop-ups.

            cls.server_thread.join(timeout=5)  # Closes the thread running our test_app.

            print(cls.server_thread.is_alive())  # Checks to see if the test_app thread is still actually active.

            # Destroy our test databases.

            db.session.remove()
            db.drop_all()

            # Remove our application and request contexts.

            cls.app_context.pop()
            cls.request_context.pop()

    def setUp(self):
        if not self.client:
            self.skipTest('Our web browser is currently not available!')

    def tearDown(self):
        pass


class TestConnections(LiveServerTestCase):
    def test_server_is_up_and_running(self):
        self.client.get(url_for('main_bp.homepage'))
        self.assertEqual(response.code, 200)
