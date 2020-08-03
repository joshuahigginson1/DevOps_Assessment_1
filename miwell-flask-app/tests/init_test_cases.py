# LiveServer is a Flask-testing tool that allows you to connect to headless browsers.
# A browser that do not render the content visually (such as Firefox or Chrome)...
# ...but executes all scripts,  styling, and simulates user interaction.

import urllib3

import os

from selenium import webdriver

from flask_testing import LiveServerTestCase

from flaskr import create_app as app_factory


# Define IndexTest, extending LiveServerTestCase - a special class we use to run our live server tests.

class BaseTest(LiveServerTestCase):

    # Inside setUp, we create a webdriver - something similar to a browser.
    # We use it to access and inspect our application through the LiveServer.

    def setUp(self):
        self.driver = webdriver.Safari()

    # tearDown makes sure our driver is closed after each test, and that our resources are released.

    def tearDown(self):
        self.driver.close()

    def create_app(self):
        os.environ['FLASK_ENV'] = 'testing'
        app = app_factory()

        # Next, we set our live server to run on a different port from the default, but that's not required.

        return app

    def test_that_server_is_running(self):
        http_response = urllib3.urlopen(self.get_server_url())
        self.assertEqual(http_response.code, 200)  # Test to check if the server is actually running and responsive.
