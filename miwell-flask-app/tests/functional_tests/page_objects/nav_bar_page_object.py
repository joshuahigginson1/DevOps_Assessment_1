# Contains the objects found on our nav bar.

# Page Objects --------------------------------------------------------------------------------------------

class NavBarPageObject(object):

    def get_dashboard_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[1]')

        button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return button_attributes

    def click_dashboard_button(self):
        get_button = self.get_dashboard_button(self)['button element']  # Retrieve the button element.
        get_button.click()  # Simulates a left click on our button element.

    def get_logout_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[4]')

        button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return button_attributes

    def click_logout_button(self):
        get_button = self.get_logout_button(self)['button element']  # Retrieve the button element.
        get_button.click()  # Simulates a left click on our button element.

    def get_settings_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[5]')

        button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return button_attributes

    def click_settings_button(self):
        get_button = self.get_settings_button(self)['button element']  # Retrieve the button element.
        get_button.click()  # Simulates a left click on our button element.


class PatientNavBarPageObject(NavBarPageObject):

    def get_my_patients_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return button_attributes

    def click_my_patients_button(self):
        get_button = self.get_my_patients_button(self)['button element']  # Retrieve the button element.
        get_button.click()  # Simulates a left click on our button element.

    def get_psych_tools_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[3]')

        button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return button_attributes

    def click_psych_tools_button(self):
        get_button = self.get_psych_tools_button(self)['button element']  # Retrieve the button element.
        get_button.click()  # Simulates a left click on our button element.


class PsychNavBarPageObject(NavBarPageObject):

    def get_my_progress_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return button_attributes

    def click_my_progress_button(self):
        get_button = self.get_my_progress_button(self)['button element']  # Retrieve the button element.
        get_button.click()  # Simulates a left click on our button element.

    def get_my_tools_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[3]')

        button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return button_attributes

    def click_my_tools_button(self):
        get_button = self.get_my_tools_button(self)['button element']  # Retrieve the button element.
        get_button.click()  # Simulates a left click on our button element.