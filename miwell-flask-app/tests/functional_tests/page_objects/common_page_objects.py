# Contains the common objects found across our web app.

# Page Objects -------------------------------


class CommonPageObject(object):
    # Define global class variables. These can be accessed by any function within our class using 'self.<variable>'

    def __init__(self, client):  # The page object is initialised with an object that represents the current test.
        self.client = client

    # This gives us the ability to make assertions and access the webdriver via self.test.client.

    def get_page_url(self):
        page_url = self.client.current_url

        return page_url

    def get_page_response(self):
        page_status_code = self.client.last_request.response.status_code

        print(f"\nThe last HTTP code request was: {page_status_code}!\n")

        return page_status_code

    def get_page_title(self):
        return self.client.title

    def get_page_footer(self):
        get_footer_element = self.client.find_element_by_xpath('/html/body/footer/h6')

        footer_attributes = {
            'text': get_footer_element.get_attribute('innerHTML'),
            'footer element': get_footer_element
        }

        return footer_attributes


class MainNavBar:
    def get_home_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[1]')

        home_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return home_button_attributes

    def get_about_button(self):
        button_label = "About"

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        about_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return about_button_attributes


class UserNavBar:

    def get_dashboard_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[1]')

        dashboard_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return dashboard_button_attributes

    def get_logout_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[4]')

        logout_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return logout_button_attributes

    def get_acc_settings_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[5]')

        settings_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return settings_button_attributes


class PatientNavBar(UserNavBar):

    def get_patient_progress_button(self):

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        patient_progress_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return patient_progress_button_attributes

    def get_patient_tools_button(self):

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[3]')

        patient_tools_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return patient_tools_button_attributes


class PsychiatristNavBar(UserNavBar):

    def get_my_patients_button(self):

        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[2]')

        my_patients_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return my_patients_button_attributes

    def get_psychiatrist_tools_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/nav/a[3]')

        psychiatrist_tools_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return psychiatrist_tools_button_attributes
