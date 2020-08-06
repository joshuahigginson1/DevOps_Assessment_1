# Contains the code to test our common page elements.

# Imports --------------------------------------------------------------------------------
from time import sleep

from flask import url_for

from tests.functional_tests.page_objects.main_page_objects.main_home_page_object import MainHomePageObject

from tests.functional_tests.test_pages.test_common_page_elements import TestCommonPageElements, \
    print_assertion_to_console


# Helper Functions ----------------------------------------------------------------------

# Helper Functions are used to prevent repeating basic lines of code within our testing.


# Tests ----------------------------------------------------------------------------------


class TestMainHomePageElements(TestCommonPageElements):
    # Common Assertions ------------------------------------------------------------------

    favicon_assertion_name = 'ying-yang'
    title_assertion = 'Homepage ~ MiWell'

    def test_forms_label_text(self):  # A test to check that the email label is correct.
        email_label_assertion = "Email"
        password_label_assertion = "Password"

        get_email_label_text = MainHomePageObject.get_email_login_field(self)['label name']
        get_password_label_text = MainHomePageObject.get_password_login_field(self)['label name']

        print_assertion_to_console('email form label text', get_email_label_text, email_label_assertion)
        print_assertion_to_console('password form label', get_password_label_text, password_label_assertion)

        self.assertEqual(get_email_label_text, email_label_assertion)
        self.assertEqual(get_password_label_text, password_label_assertion)


class TestAboutPageElements(TestCommonPageElements):
    # Common Assertions ------------------------------------------------------------------

    favicon_assertion_name = 'ying-yang'
    title_assertion = 'About ~ MiWell'

    pass


class TestPatientRegisterPageElements(TestCommonPageElements):
    # Common Assertions ------------------------------------------------------------------

    favicon_assertion_name = 'ying-yang'
    title_assertion = 'Register ~ MiWell'

    pass


class TestPsychRegisterPageElements(TestCommonPageElements):
    # Common Assertions ------------------------------------------------------------------

    favicon_assertion_name = 'ying-yang'
    title_assertion = 'Register Psychiatrist ~ MiWell'

    pass
