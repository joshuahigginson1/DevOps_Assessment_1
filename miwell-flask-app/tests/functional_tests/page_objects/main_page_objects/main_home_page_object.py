# Contains the objects found on our home page.

# Imports -------------------------------------------------------------------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject, MainNavBar


# Page Objects --------------------------------------------------------------------------------------------


class MainHomePageObject(CommonPageObject, MainNavBar):  # A class for every object pertaining to our main home page.

    # Default Page Variables.

    user_email = 'Email@gmail.com'
    user_password = 'Default Password'

    def get_email_login_field(self):  # A function to return the attributes of our email login field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="email"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[1]/label')

        email_login_form_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return email_login_form_attributes

    def type_in_email_form(self, input_to_type=user_email):  # A function to type text into our email form box.

        # Retrieve our form attributes.

        get_field_attributes = MainHomePageObject.get_email_login_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def clear_email_form(self):  # A function to clear the text from within our email form box.

        # Retrieve our form attributes.

        get_field_attributes = MainHomePageObject.get_email_login_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        get_field_element.clear()  # Clears our form.

        print(f"Running Simulation: Currently clearing the {get_field_label} field.")

    def get_password_login_field(self):  # A function to return the attributes of our password login field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="password"]'),
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[2]/label')

        password_login_form_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return password_login_form_attributes

    def type_in_password_form(self, input_to_type=user_password):  # A function to type text into our password form box.

        # Retrieve our form attributes.

        get_field_attributes = MainHomePageObject.get_password_login_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def clear_password_form(self):  # A function to clear the text from within our password form box.

        # Retrieve our form attributes.

        get_field_attributes = MainHomePageObject.get_password_login_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        get_field_element.clear()  # Clears our form.

        print(f"Running Simulation: Currently clearing the {get_field_label} field.")

    def get_remember_me(self):  # A function to retrieve the attributes of our remember me checkbox.

        get_checkbox_element = self.test.client.find_element_by_xpath('/html/body/div[2]/form/div[3]')
        get_label_element = self.test.client.find_element_by_xpath('/html/body/div[2]/form/div[3]/label')

        remember_me_checkbox_attributes = {
            'checkbox element': get_checkbox_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element,
            'is box selected': get_label_element.is_selected()  # If the box is selected, return True.
        }

        return remember_me_checkbox_attributes

    def remember_me_click(self):  # Module to simulate clicking on the remember me checkbox.

        get_checkbox_element = self.get_remember_me()['checkbox element']
        get_checkbox_element.Click()

    def get_login_button(self):  # A function to retrieve the attributes of our login button.

        get_button_element = self.client.find_element_by_xpath('//*[@id="submit"]')

        login_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return login_button_attributes

    def click_login_button(self):
        get_login_button_element = self.get_login_button['button element']
        get_login_button_element.click()

    def get_register_button(self):

        get_button_element = self.client.find_element_by_xpath('/html/body/a[1]')

        register_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return register_button_attributes

    def click_register_button(self):
        get_register_button_element = self.get_login_button['button element']
        get_register_button_element.click()