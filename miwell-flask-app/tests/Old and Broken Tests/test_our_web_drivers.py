# This file creates the default TestCase base classes.

# Here is the sequence of how the functional tests should run:

# 1. Create a new Flask application.
# 2. Initialise our test database.
# 3. Run our unit and integration tests.
# 4. Destroy the test database.
# 5. Stop the Flask application.

# Imports ------------------------------------------------------------------------------------
from selenium import webdriver
import time

# Create the Default Unit Test Class ------------------------------------------------------------------------

# Here, we inherit from LiveServerTestCase, an expansion of the TestCase module from flask_testing.
# It has a number of extra features which make it useful for integration testing with Selenium.


driver = webdriver.Safari()  # Here, we set up a new instance of our selenium web driver.
driver.maximize_window()
driver.get('https://www.google.com')

search_ele = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_ele.send_keys("Hello Bitches")

time.sleep(3)

driver.quit()
