# Contains the common objects found across our web app.

# Page Objects -------------------------------


class CommonPageObject(object):
    # Define global class variables. These can be accessed by any function within our class using 'self.<variable>'

    def __init__(self, test):  # The page object is initialised with an object that represents the current test.
        self.test = test

    # This gives us the ability to make assertions and access the webdriver via self.test.client.

    def get_test_title(self):
        return self.test.client.title

    def get_test_footer(self):
        return self.test.client.find_element_by_xpath('/html/body/footer/footer/h6')


class MainNavBar:
    def get_home_button(self):
        button_label = "Home"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[1]')

    def get_about_button(self):
        button_label = "About"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[2]')


class UserNavBar:

    def get_dashboard_button(self, driver):
        button_label = "Dashboard"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[1]')

    def get_logout_button(self):
        button_label = "Log Out"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[4]')

    def get_settings_button(self):
        button_label = "Settings"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[5]')


class PatientNavBar(UserNavBar):

    def get_patient_progress_button(self):
        button_label = "My Progress"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[2]')

    def get_patient_tools_dashboard_button(self):
        button_label = "My Tools"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[3]')


class PsychiatristNavBar(UserNavBar):

    def get_my_patients_button(self):
        button_label = "My Patients"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[2]')

    def get_patient_tools_dashboard_button(self):
        button_label = "Patient Tools"
        return self.test.client.find_element_by_xpath('/html/body/nav/a[3]')

    # Add to test file.

    # assert self.page_title in self.test.client.title

    # assert "By Joshua Higginson for QA Consulting" in footer
