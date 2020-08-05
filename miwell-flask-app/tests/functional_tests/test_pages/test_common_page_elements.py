# Contains the code to test our common page elements.

# Imports --------------------------------------------------------------------------------

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject

from tests.functional_tests.functional_test_framework import LiveServerTestCase


# Tests ----------------------------------------------------------------------------------

class TestCommonPageElements(LiveServerTestCase):

    title = None
    footer = "By Joshua Higginson for QA Consulting"

    def test_title(self):
        self.assertEqual(self, CommonPageObject.get_test_title(), self.title)

    def test_footer(self):
        page_object = CommonPageObject(self.client)
        self.assertEqual(page_object.get_test_footer(), self.footer)
