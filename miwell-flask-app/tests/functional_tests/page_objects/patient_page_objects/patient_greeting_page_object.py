# Contains the objects found on our user greetings page.

# Imports --------------------------------------------------------------------------------


# Page Objects ---------------------------------------------------------------------------

class PatientGreetingPageObject(object):

    bio = 'This is a test bio.'

    def get_current_feeling_buttons(self):

        feeling1element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-0"]')
        feeling2element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-1"]')
        feeling3element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-2"]')
        feeling4element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-3"]')
        feeling5element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-4"]')
        feeling6element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-5"]')
        feeling7element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-6"]')
        feeling8element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-7"]')
        feeling9element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-8"]')
        feeling10element = self.client.find_element_by_xpath('// *[ @ id = "current_feeling-9"]')

        attributes = {
            'feeling1 element': feeling1element,
            'feeling2 element': feeling2element,
            'feeling3 element': feeling3element,
            'feeling4 element': feeling4element,
            'feeling5 element': feeling5element,
            'feeling6 element': feeling6element,
            'feeling7 element': feeling7element,
            'feeling8 element': feeling8element,
            'feeling9 element': feeling9element,
            'feeling10 element': feeling10element
        }

        return attributes

    def click_feeling1_button(self):
        self.get_current_feeling_buttons(self)['feeling1 element'].click()

    def click_feeling2_button(self):
        self.get_current_feeling_buttons(self)['feeling2 element'].click()

    def click_feeling3_button(self):
        self.get_current_feeling_buttons(self)['feeling3 element'].click()

    def click_feeling4_button(self):
        self.get_current_feeling_buttons(self)['feeling4 element'].click()

    def click_feeling5_button(self):
        self.get_current_feeling_buttons(self)['feeling5 element'].click()

    def click_feeling6_button(self):
        self.get_current_feeling_buttons(self)['feeling6 element'].click()

    def click_feeling7_button(self):
        self.get_current_feeling_buttons(self)['feeling7 element'].click()

    def click_feeling8_button(self):
        self.get_current_feeling_buttons(self)['feeling8 element'].click()

    def click_feeling9_button(self):
        self.get_current_feeling_buttons(self)['feeling9 element'].click()

    def click_feeling10_button(self):
        self.get_current_feeling_buttons(self)['feeling10 element'].click()

    def get_feeling_comparison_buttons(self):

        attributes = {
            'worse element': self.client.find_element_by_xpath('//*[@id="feeling_comparison-0"]'),
            'same element': self.client.find_element_by_xpath('//*[@id="feeling_comparison-1"]'),
            'better element': self.client.find_element_by_xpath('//*[@id="feeling_comparison-2"]'),
        }

        return attributes

    def click_worse_button(self):
        self.get_feeling_comparison_buttons(self)['worse element'].click()

    def click_same_button(self):
        self.get_feeling_comparison_buttons(self)['same element'].click()

    def click_better_button(self):
        self.get_feeling_comparison_buttons(self)['better element'].click()

    def get_behaviour_buttons(self):

        attributes = {
            'happy element': self.client.find_element_by_xpath('//*[@id="behaviours-0"]'),
            'angry element': self.client.find_element_by_xpath('//*[@id="behaviours-1"]'),
            'disappointed element': self.client.find_element_by_xpath('//*[@id="behaviours-2"]'),
            'done with today element': self.client.find_element_by_xpath('//*[@id="behaviours-3"]'),
            'persevering element': self.client.find_element_by_xpath('//*[@id="behaviours-4"]'),
            'anxious element': self.client.find_element_by_xpath('//*[@id="behaviours-5"]'),
            'confused element': self.client.find_element_by_xpath('//*[@id="behaviours-6"]'),
            'worried element': self.client.find_element_by_xpath('//*[@id="behaviours-7"]'),
            'ill element': self.client.find_element_by_xpath('//*[@id="behaviours-8"]'),
            'exhausted element': self.client.find_element_by_xpath('//*[@id="behaviours-9"]'),
            'accomplished element': self.client.find_element_by_xpath('//*[@id="behaviours-10"]'),
            'star struck element': self.client.find_element_by_xpath('//*[@id="behaviours-11"]'),
            'frightened element': self.client.find_element_by_xpath('//*[@id="behaviours-12"]'),
        }

        return attributes

    def click_happy_element(self):
        self.get_behaviour_buttons(self)['happy element'].click()

    def click_angry_element(self):
        self.get_behaviour_buttons(self)['angry element'].click()

    def click_disappointed_element(self):
        self.get_behaviour_buttons(self)['disappointed element'].click()

    def click_done_with_today_element(self):
        self.get_behaviour_buttons(self)['done with today element'].click()

    def click_persevering_element(self):
        self.get_behaviour_buttons(self)['persevering element'].click()

    def click_anxious_element(self):
        self.get_behaviour_buttons(self)['anxious element'].click()

    def click_confused_element(self):
        self.get_behaviour_buttons(self)['confused element'].click()

    def click_worried_element(self):
        self.get_behaviour_buttons(self)['worried element'].click()

    def click_ill_element(self):
        self.get_behaviour_buttons(self)['ill element'].click()

    def click_exhausted_element(self):
        self.get_behaviour_buttons(self)['exhausted element'].click()

    def click_accomplished_element(self):
        self.get_behaviour_buttons(self)['accomplished element'].click()

    def click_star_struck_element(self):
        self.get_behaviour_buttons(self)['star struck element'].click()

    def click_frightened_element(self):
        self.get_behaviour_buttons(self)['frightened element'].click()

    def get_bio_element(self):
        return self.client.find_element_by_xpath('//*[@id="patient_comment"]')

    def type_in_bio_form(self, input_to_type=bio):  # A function to type text into our bio form box.

        # Retrieve our form attributes.

        get_field_element = self.get_bio_element()

        # After retrieving the field element, simulate typing into a form box.

        get_field_element.send_keys(input_to_type)
        print(f"Running Simulation: Currently typing '{input_to_type}' in the bio field.")

    def clear_password_form(self):  # A function to clear the text from within our password form box.

        # Retrieve our form attributes.

        get_field_element = self.get_bio_element()
        get_field_element.clear()  # Clears our form.

        print(f"Running Simulation: Currently clearing the bio field.")

    def get_submit_button(self):
        return self.client.find_element_by_xpath('//*[@id="submit"]')

    def click_submit_button(self):
        self.get_submit_button(self).click()

    def get_skip_evaluation_button(self):
        return self.client.find_element_by_xpath('/html/body/p/a')

    def click_skip_evaluation_button(self):
        return self.get_skip_evaluation_button(self).click()



