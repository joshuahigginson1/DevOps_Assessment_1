# Contains the objects found on our home page.

# Imports -------------------------------------------------------------------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject, MainNavBar


# Page Objects --------------------------------------------------------------------------------------------


class HomePageObject(CommonPageObject, MainNavBar):

    def get_email_login_field(self):
        email_login_form = {
            'Field': self.test.client.find_element_by_xpath('//*[@id="email"]'),
            'Label': self.test.client.find_element_by_xpath('/html/body/div[2]/form/div[1]/label')
        }
        return email_login_form

    def get_password_login_field(self):
        password_login_form = {
            'Field': self.test.client.find_element_by_xpath('//*[@id="password"]'),
            'Label': self.test.client.find_element_by_xpath('/html/body/div[2]/form/div[2]/label')
        }
        return password_login_form

    def get_remember_me(self):
        remember_me = {
            'CheckBox': self.test.client.find_element_by_xpath('/html/body/div[2]/form/div[3]'),
            'Label': self.test.client.find_element_by_xpath('/html/body/div[2]/form/div[3]/label')
        }

        return remember_me

    def get_login_button(self):
        return self.test.client.find_element_by_xpath('//*[@id="submit"]')

    def get_register_button(self):
        return self.test.client.find_element_by_xpath('/html/body/a[1]')
