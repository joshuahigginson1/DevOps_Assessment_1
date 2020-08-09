# Contains the objects found on any of our error pages.

# Imports -------------------------------------------------------------------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject


# Page Objects --------------------------------------------------------------------------------------------

class HomePageObject(CommonPageObject):

    def get_random_error_remark(self):

        get_page_element = self.test.client.find_element_by_xpath('/html/body/h1')

        attributes = {
            'page label': get_page_element.get_attribute('innerHTML'),
            'page element': get_page_element
        }

        return attributes

    def error_code_response(self):
        get_page_element = self.test.client.find_element_by_xpath('/html/body/p')

        attributes = {
            'page label': get_page_element.get_attribute('innerHTML'),
            'page element': get_page_element
        }

        return attributes

    def random_error_photo(self):
        get_page_element = self.test.client.find_element_by_xpath('/html/body/img')

        attributes = {
            'page label': get_page_element.get_attribute('innerHTML'),
            'page element': get_page_element
        }

        return attributes

    def get_back_button(self):
        get_page_element = self.test.client.find_element_by_xpath('/html/body/a')

        attributes = {
            'button label': get_page_element.get_attribute('innerHTML'),
            'button element': get_page_element
        }

        return attributes

    def click_back_button(self):
        get_back_button = self.get_back_button()['button element']
        get_back_button.click()  # Simulates a button click.


