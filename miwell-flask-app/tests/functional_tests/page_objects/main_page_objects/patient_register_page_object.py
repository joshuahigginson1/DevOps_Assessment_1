# Contains the objects found on our patient register page.

# Imports -------------------------------------------------------------------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject, PatientNavBar

# Page Objects --------------------------------------------------------------------------------------------


class PatientRegisterPageObject(CommonPageObject, PatientNavBar):
    # Default Page Variables.

    username = 'DefaultPatient'
    user_email = 'Email@gmail.com'
    user_password = 'Default Password'
    user_first_name = 'Default'
    user_last_name = 'Patient'
    user_phone_number = '07777777777'
    user_postcode = 'L1 1AA'
    user_medical_conditions = 'Robotitis. I require constant love and attention. Prone to flashing.'

    def get_username_field(self):  # A function to return the attributes of our username register field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="username"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[1]/label')

        username_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return username_field_attributes

    def type_in_username_form(self, input_to_type=username):  # A function to type text into our username form box.

        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_username_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_email_field(self):  # A function to return the attributes of our email field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="email"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[2]/label')

        email_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return email_field_attributes

    def type_in_email_form(self, input_to_type=user_email):  # A function to type text into our email form box.

        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_email_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_new_password_field(self):  # A function to return the attributes of our new password field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="password"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[3]/label')

        new_password_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return new_password_field_attributes

    def type_in_new_password_form(self,
                                  input_to_type=user_password):  # A function to type text into our password form box.

        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_new_password_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_confirm_password_field(self):  # A function to return the attributes of our confirm password field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="confirm_password"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[4]/label')

        confirm_password_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return confirm_password_field_attributes

    def type_in_confirm_password_form(self, input_to_type=user_password):
        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_confirm_password_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_first_name_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="first_name"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[5]/label')

        first_name_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return first_name_field_attributes

    def type_in_first_name_form(self, input_to_type=user_first_name):
        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_first_name_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_last_name_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="last_name"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[6]/label')

        last_name_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return last_name_field_attributes

    def type_in_last_name_form(self, input_to_type=user_last_name):
        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_last_name_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_phone_number_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="phone_number"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[7]/label')

        phone_number_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return phone_number_field_attributes

    def type_in_phone_number_form(self, input_to_type=user_phone_number):
        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_phone_number_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_postcode_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="postcode"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[8]/label')

        postcode_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return postcode_field_attributes

    def type_in_postcode_form(self, input_to_type=user_postcode):
        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_postcode_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_medical_conditions_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="medical_conditions"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[9]/label')

        medical_conditions_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return medical_conditions_field_attributes

    def type_in_medical_conditions_form(self, input_to_type=user_medical_conditions):
        # Retrieve our form attributes.

        get_field_attributes = PatientRegisterPageObject.get_medical_conditions_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_submit_button(self):
        get_button_element = self.client.find_element_by_xpath('//*[@id="submit"]')

        submit_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return submit_button_attributes

    def click_submit_button(self):
        get_submit_button_element = self.get_submit_button()['button element']
        get_submit_button_element.click()

    def get_already_registered_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/a[1]')

        already_registered_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }

        return already_registered_button_attributes

    def click_already_registered_button(self):
        get_already_registered_button_element = self.get_already_registered_button()['button element']
        get_already_registered_button_element.click()

    def get_register_as_psych_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/a[2]')

        register_as_psychiatrist_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }
        return register_as_psychiatrist_button_attributes

    def click_register_as_psychiatrist_button(self):
        get_register_as_psych_button_element = self.get_register_as_psych_button()['button element']
        get_register_as_psych_button_element.click()
