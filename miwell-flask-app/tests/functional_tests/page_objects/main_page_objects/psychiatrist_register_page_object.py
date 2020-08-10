# Contains the objects found on our psychiatrist register page.

# Imports -------------------------------------------------------------------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject, PsychiatristNavBar

# Page Objects --------------------------------------------------------------------------------------------


class PsychiatristRegisterPageObject(CommonPageObject, PsychiatristNavBar):
    # Default Page Variables.

    user_email = 'Email@gmail.com'
    user_password = 'Default Password'
    user_first_name = 'Default'
    user_last_name = 'Psychiatrist'
    bacp_number = '1616161616161616'
    user_phone_number = '07777777777'
    user_postcode = 'L1 7DQ'
    psychiatrist_bio = 'I am a robot. Not a registered psychiatrist.'

    def get_email_field(self):  # A function to return the attributes of our email field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="email"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[1]/label')

        email_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return email_field_attributes

    def type_in_email_form(self, input_to_type=user_email):  # A function to type text into our email form box.

        # Retrieve our form attributes.

        get_field_attributes = PsychiatristRegisterPageObject.get_email_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def clear_email_form(self):

        # Retrieve our form attributes.

        get_field_element = self.get_email_field()['field element']
        get_field_element.clear()  # Clears our form.

    def get_new_password_field(self):  # A function to return the attributes of our new password field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="password"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[2]/label')

        new_password_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return new_password_field_attributes

    def type_in_new_password_field(self, input_to_type=user_password):  # A function to type text into our password form box.

        # Retrieve our form attributes.

        get_field_attributes = PsychiatristRegisterPageObject.get_new_password_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def clear_new_password_field(self):

        # Retrieve our form attributes.

        get_field_element = self.get_new_password_field()['field element']
        get_field_element.clear()  # Clears our form.

    def get_confirm_password_field(self):  # A function to return the attributes of our confirm password field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="confirm_password"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[3]/label')

        confirm_password_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return confirm_password_field_attributes

    def type_in_confirm_password_form(self, input_to_type=user_password):
        # Retrieve our form attributes.

        get_field_attributes = PsychiatristRegisterPageObject.get_confirm_password_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def clear_confirm_password_field(self):

        # Retrieve our form attributes.

        get_field_element = self.get_confirm_password_field()['field element']
        get_field_element.clear()  # Clears our form.

    def get_first_name_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="first_name"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[4]/label')

        first_name_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return first_name_field_attributes

    def type_in_first_name_form(self, input_to_type=user_first_name):
        # Retrieve our form attributes.

        get_field_attributes = PsychiatristRegisterPageObject.get_first_name_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def clear_first_name_field(self):

        # Retrieve our form attributes.

        get_field_element = self.get_new_password_field()['field element']
        get_field_element.clear()  # Clears our form.

    def get_last_name_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="last_name"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[5]/label')

        last_name_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return last_name_field_attributes

    def type_in_last_name_form(self, input_to_type=user_last_name):
        # Retrieve our form attributes.

        get_field_attributes = PsychiatristRegisterPageObject.get_last_name_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_bacp_field(self):  # A function to return the attributes of our username register field.

        get_field_element = self.client.find_element_by_xpath('//*[@id="bacp_number"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[6]/label')

        bacp_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return bacp_field_attributes

    def type_in_bacp_form(self, input_to_type=bacp_number):  # A function to type text into our bacp form box.

        # Retrieve our form attributes.

        get_field_attributes = PsychiatristRegisterPageObject.get_bacp_field(self)
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

        get_field_attributes = PsychiatristRegisterPageObject.get_phone_number_field(self)
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

        get_field_attributes = PsychiatristRegisterPageObject.get_postcode_field(self)
        get_field_element = get_field_attributes['field element']
        get_field_label = get_field_attributes['label name']

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the {get_field_label} field.")

    def get_psychiatrist_bio_field(self):
        get_field_element = self.client.find_element_by_xpath('//*[@id="psychiatrist_bio"]')
        get_label_element = self.client.find_element_by_xpath('/html/body/div[2]/form/div[9]/label')

        psychiatrist_bio_field_attributes = {
            'field element': get_field_element,
            'label name': get_label_element.get_attribute('innerHTML'),
            'label element': get_label_element
        }

        return psychiatrist_bio_field_attributes

    def type_in_psychiatrist_bio_form(self, input_to_type=psychiatrist_bio):
        # Retrieve our form attributes.

        get_field_attributes = PsychiatristRegisterPageObject.get_psychiatrist_bio_field(self)
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

    def get_register_as_patient_button(self):
        get_button_element = self.client.find_element_by_xpath('/html/body/a[2]')

        register_as_patient_button_attributes = {
            'button label': get_button_element.get_attribute('innerHTML'),
            'button element': get_button_element
        }
        return register_as_patient_button_attributes

    def click_register_as_patient_button(self):
        get_register_as_patient_button_element = self.get_register_as_patient_button()['button element']
        get_register_as_patient_button_element.click()






