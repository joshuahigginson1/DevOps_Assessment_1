# Contains the common objects found across our web app.

# Page Objects -------------------------------


class CommonPageObject(object):  # A class to contain common functions, shared among multiple pages of our site.

    # Define global class variables. These can be accessed by any function within our class using 'self.<variable>'

    def __init__(self, client):  # The page object is initialised with an object that represents the current test.
        self.client = client

    # This gives us the ability to make assertions and access the webdriver via self.test.client.

    def get_page_url(self):  # A function which returns the current page URL.
        page_url = self.client.current_url

        return page_url

    def get_page_response(self):  # A function which returns the last received HTTP status code.
        page_status_code = self.client.last_request.response.status_code

        print(f"\nThe last HTTP code request was: {page_status_code}!\n")

        return page_status_code

    def get_page_title(self):  # A function to return the current page's title, that has been rendered from our browser.
        return self.client.title

    def get_page_footer(self):  # A function to return the attributes associated with our page footer.
        get_footer_element = self.client.find_element_by_xpath('/html/body/footer/h6')

        footer_attributes = {
            'text': get_footer_element.get_attribute('innerHTML'),
            'footer element': get_footer_element
        }

        return footer_attributes

    def get_favicon_element(self):  # A function to return the favicon's attributes.
        get_favicon_element = self.client.find_element_by_class_name('favicon')

        favicon_attributes = {
            'name': get_favicon_element.get_attribute('name'),
            'href': get_favicon_element.get_attribute('href'),
            'favicon element': get_favicon_element
        }
        return favicon_attributes


class MainNavBar:  # A class which contains functions pertaining to our main nav bar.

    def get_home_button(self):  # A function to retrieve the attributes of our login button.

        # Retrieve our button element from it's xpath link.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[1]')

        home_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),  # Gets the text found within two html tags.
            'button element': get_button_element
        }

        return home_button_attributes  # Returns the attributes of our home button as a dictionary.

    def click_home_button(self):  # Module to simulate clicking on the home button.

        get_home_button = self.get_home_button(self)['button element']  # Retrieve the button element.
        get_home_button.click()  # Simulates a left click on our button element.

    def get_about_button(self):  # Module to simulate clicking on the about button.

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        about_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return about_button_attributes

    def click_about_button(self):
        get_about_button = self.get_about_button(self)['button element']  # Retrieve the button element.
        get_about_button.click()  # Simulates a left click on our button element.


class UserNavBar:  # A class which contains shared functions between the Patient nav bar and the Psychiatrist nav bar.

    def get_dashboard_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[1]')

        dashboard_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return dashboard_button_attributes

    def click_dashboard_button(self):

        get_patient_dashboard_button = self.get_dashboard_button['button element']
        get_patient_dashboard_button.click()  # Simulates a button click

    def get_logout_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[4]')

        logout_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return logout_button_attributes

    def click_logout_button(self):
        get_logout_button = self.get_logout_button()['button element']
        get_logout_button.click()  # Simulates a button click

    def get_acc_settings_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[5]')

        settings_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return settings_button_attributes

    def click_acc_settings_button(self):
        get_acc_settings_button = self.get_acc_settings_button()['button element']
        get_acc_settings_button.click()  # Simulates a button click


class PatientNavBar(UserNavBar):  # A class which contains the functions dedicated to our Patient nav bar.

    def get_patient_progress_button(self):

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        patient_progress_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return patient_progress_button_attributes

    def click_patient_progress_button(self):
        get_patient_progress_button = self.get_patient_progress_button()['button element']
        get_patient_progress_button.click()  # Simulates a button click

    def get_patient_tools_button(self):

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[3]')

        patient_tools_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return patient_tools_button_attributes

    def click_patient_tools_button(self):
        get_patient_tools_button = self.get_patient_tools_button()['button element']
        get_patient_tools_button.click()  # Simulates a button click


class PsychiatristNavBar(UserNavBar):  # A class which contains the functions dedicated to our Psychiatrist nav bar.

    def get_my_patients_button(self):

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        my_patients_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return my_patients_button_attributes

    def click_my_patients_button(self):
        get_my_patients_button = self.get_my_patients_button()['button element']
        get_my_patients_button.click()  # Simulates a button click.

    def get_psychiatrist_tools_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[3]')

        psychiatrist_tools_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return psychiatrist_tools_button_attributes

    def click_psychiatrist_tools_button(self):
        get_psychiatrist_tools_button = self.get_psychiatrist_tools_button()['button element']
        get_psychiatrist_tools_button.click()  # Simulates a button click.
