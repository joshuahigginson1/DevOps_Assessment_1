# Imports -----------------------------------------------------------------------------------------------------

import flask
from seleniumwire import webdriver

import unittest

from flaskr import create_app, db
import threading
import time

# Integration Test Framework --------------------------------------------------------------------------------


class LiveServerTestCase(unittest.TestCase):
    client = None

    @classmethod  # At the very start of the tests, we must set up a Class.
    def setUpClass(cls):

        try:
            cls.client = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")  # DEPENDENT ON RUN ENVIRON.

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

            cls.root_url = 'http://localhost:5000'  # WE MUST CHANGE THIS VARIABLE MANUALLY DEPENDING ON THE HOST AND WE ARE USING.

            db.create_all()  # Creates our database.

            cls.url_root = flask.request.base_url  # Sets the root url for the currently running server.

            # Configures our app to run in a new thread.
            cls.server_thread = threading.Thread(name="TestInstance", target=cls.test_app.run)
            cls.server_thread.start()  # Runs our test_app on a new thread.

            time.sleep(1)  # Give the server a second to ensure it is up, before running any tests prematurely.

    def setUp(self):
        if not self.client:
            self.skipTest('Our web browser is currently not available!')

    def test_server_is_up_and_running(self):
        print(f"the currently set root url is: {self.url_root}")
        self.assertEqual(self.client.last_request.response.status_code, 200)

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # Stop our flask server, and close our browser.
            cls.client.get(f'{cls.root_url}/shutdown')
            time.sleep(1)
            cls.client.quit()  # .quit() is used to exit the browser, end the session, tabs, pop-ups.

            cls.server_thread.join(timeout=5)  # Closes the thread running our test_app.

            if not cls.server_thread.is_alive():
                print("The server thread rejoined successfully.")
            else:
                raise RuntimeWarning("The server thread is somehow still active after ending our tests.")

            # Destroy our test databases.

            db.session.remove()
            db.drop_all()

            # Remove our application and request contexts.

            cls.app_context.pop()
            cls.request_context.pop()