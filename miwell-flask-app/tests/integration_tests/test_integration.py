# This script manages the integration testing for <DEFAULT>.

# Our script must start with the prefix 'test_', like in Pytest.

# Here is the sequence of how the functional tests should run:

# 1. Create a new Flask application.
# 2. Initialise our test database.
# 3. Run our unit tests.
# 4. Destroy the test database.
# 5. Stop the Flask application.

# Imports -------------------------------------------------------------------------------------------------

# Import our suite of testing tools.
import unittest
import flask_testing
import selenium

# Here, we import our default test objects from ./flask-app/tests/__init__.py
from tests import DefaultIntegrationTestClass

import config  # Imports our app config.py file.


# Create our integration Tests ----------------------------------------------------------------------------

class IntegrationTestTemplate(DefaultIntegrationTestClass):  # Create a new integration test class.

    # We have already defined our set up and tear down methods. We don't need to worry about creating them again.
    # Each test must be defined with the starting prefix 'test_'. Just like in PyTest.

    def test_example(self):  # Define a new test.
        # Our test code goes here.
        pass


# Run our Test Script ---------------------------------------------------------------------------------------

# To execute all of the tests in this file at once, we need two lines of code at the end of each test.py file.
# These lines are very similar to the lines which we use to run a flask app.


if __name__ == '__main__':
    unittest.main(host='0.0.0.0', port=5000)
