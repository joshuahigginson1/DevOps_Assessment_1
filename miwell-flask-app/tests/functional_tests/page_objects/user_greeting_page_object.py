# Contains all of the code associated with our user greeting page.

# Imports ------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject

# Page Object Class --------------------------


class UserGreetingPageObject(CommonPageObject):

    def greeting_header(self):
        return self.test.client.find_element_by_xpath('/html/body/h1')

    def email_label(self):
        return self.test.client.find_element_by_xpath('//*[@id="email"]')

    def password_textbox(self):
        return self.test.client.find_element_by_xpath('//*[@id="password"]')

    def remember_me_checkbox(self):
        return self.test.client.find_element_by_xpath('//*[@id="remember"]')

    def login_button(self):
        return self.test.client.find_element_by_xpath('//*[@id="submit"]')

    def register_link(self):
        return self.test.client.find_element_by_xpath('/html/body/a')
