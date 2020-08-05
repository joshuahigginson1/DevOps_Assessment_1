# Contains the objects found on any of our error pages.

# Imports -------------------------------------------------------------------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject


# Page Objects --------------------------------------------------------------------------------------------

class HomePageObject(CommonPageObject):

    def random_error_remark(self):
        return self.test.client.find_element_by_xpath('/html/body/h1')

    def error_code_response(self):
        return self.test.client.find_element_by_xpath('/html/body/p')

    def random_error_photo(self):
        return self.test.client.find_element_by_xpath('/html/body/img')

    def get_back_button(self):
        return self.test.client.find_element_by_xpath('/html/body/a')
