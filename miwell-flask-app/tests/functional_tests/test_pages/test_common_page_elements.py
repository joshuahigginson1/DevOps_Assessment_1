# Contains the code to test our common page elements.

# Imports --------------------------------------------------------------------------------
from flask import url_for

from tests.functional_tests.page_objects.common_page_objects import CommonPageObject, MainNavBar, PatientNavBar, \
    PsychiatristNavBar

from tests.functional_tests.functional_test_framework import LiveServerTestCase


# Helper Functions ----------------------------------------------------------------------

# Helper Functions are used to prevent repeating basic lines of code within our testing.

def print_assertion_to_console(element_to_test, test_outcome, assertion):
    print(f'ASSERTION: The current {element_to_test} should be: {assertion}!\n')
    print(f'OUTCOME: The current {element_to_test} is actually: {test_outcome}!\n')


def compare_and_evaluate_relative_urls(test_outcome, endpoint_bp):
    print(f'The root URL is: {LiveServerTestCase.root_url}\n')  # Here, we retrieve the root URL from our webdriver.

    # We ask the developer for the test's expected endpoint, and get it's relative associated URL with the url_for function.
    expected_endpoint = url_for(endpoint_bp)

    # We run string concatenation to generate the absolute URL associated with our endpoint.
    full_endpoint_url = f'{LiveServerTestCase.root_url}{expected_endpoint}'

    print(f'Expected URL: {full_endpoint_url}\n')
    print(f'Test Outcome: {test_outcome}\n')

    if full_endpoint_url == test_outcome:  # If the test outcome matches expected endpoint URL, then return true.
        return True
    else:
        return False


# Tests ----------------------------------------------------------------------------------

class TestCommonPageElements(LiveServerTestCase):

    # Assertions -----------------------------------------------------------------

    favicon_assertion_name = None
    title_assertion = None
    footer_assertion = "By Joshua Higginson for QA Consulting"

    # Element Specific Tests ----------------------------------------------------

    def test_page_favicon(self):  # A test to check that the correct favicon is displaying.
        get_favicon_name = CommonPageObject.get_favicon_element(self)['name']  # Retrieve favicon name.

        print_assertion_to_console('page favicon', get_favicon_name, self.favicon_assertion_name)

        self.assertEqual(get_favicon_name, self.favicon_assertion_name)  # Make test assertion.

    def test_page_title(self):  # A test to check that the title of our page is correct.
        get_page_title = CommonPageObject.get_page_title(self)  # Retrieve the page title.

        print_assertion_to_console('page title', get_page_title, self.title_assertion)

        self.assertEqual(get_page_title, self.title_assertion)

    def test_page_footer(self):    # A test to check that the page footer is correct.
        get_page_footer = CommonPageObject.get_page_footer(self)['text']  # Retrieve text from page footer.

        print_assertion_to_console('page footer', get_page_footer, self.footer_assertion)

        self.assertEqual(get_page_footer, self.footer_assertion)


class TestMainNavBar(LiveServerTestCase):

    # Element Specific Tests ----------------------------------------------------

    def test_home_button_label(self):  # A test to check that our button is correctly labeled.
        button_label_assertion = "Home"  # Declare our assertion criteria.

        get_home_button = MainNavBar.get_home_button(self)['button label']  # Retrieve the button label.

        print_assertion_to_console('home button', get_home_button, button_label_assertion)

        self.assertEqual(get_home_button, button_label_assertion)

    def test_home_button_click(self):    # A test to check the functionality of clicking the 'about' button.

        MainNavBar.click_home_button()

        page_status_code = CommonPageObject.get_page_response(self)  # Get the current page's status code.

        self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

        page_url = CommonPageObject.get_page_url(self)  # Get the current page's url.

        self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'main_bp.homepage'))  # Make our assertion.

    def test_about_button_label(self):  # A test to check that our button is correctly labeled.
        button_label_assertion = "About"

        get_about_button = MainNavBar.get_about_button(self)['button label']

        print_assertion_to_console('about button', get_about_button, button_label_assertion)

        self.assertEqual(get_about_button, button_label_assertion)

    def test_about_button_click(self):  # A test to check the functionality of clicking the 'about' button.

        MainNavBar.click_home_button()

        page_status_code = CommonPageObject.get_page_response(self)

        self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

        page_url = CommonPageObject.get_page_url(self)

        self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'main_bp.about'))


class TestPatientNavBar(LiveServerTestCase):

    # Element Specific Tests ----------------------------------------------------

    def test_patient_dashboard_button_label(self):
        button_label_assertion = "Dashboard"

        get_patient_dashboard_button = PatientNavBar.get_dashboard_button(self)['button label']

        print_assertion_to_console('patient dashboard button', get_patient_dashboard_button, button_label_assertion)

        self.assertEqual(get_patient_dashboard_button, button_label_assertion)

    def test_patient_dashboard_button_click(self):

        PatientNavBar.click_dashboard_button()

        page_status_code = CommonPageObject.get_page_response(self)

        self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

        page_url = CommonPageObject.get_page_url(self)

        self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'dashboard_bp.dashboard'))

    def test_patient_progress_button_label(self):
        button_label_assertion = "My Progress"

        get_patient_progress_button = PatientNavBar.get_patient_progress_button(self)['button label']

        print_assertion_to_console('my progress button', get_patient_progress_button, button_label_assertion)

        self.assertEqual(get_patient_progress_button, button_label_assertion)

    def test_patient_progress_button_click(self):

        PatientNavBar.click_patient_progress_button()

        page_status_code = CommonPageObject.get_page_response(self)

        self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

        page_url = CommonPageObject.get_page_url(self)

        self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'dashboard_bp.user_progress'))

    def test_patient_tools_button_label(self):
        button_label_assertion = "My Tools"

        get_patient_tools_button = PatientNavBar.get_patient_tools_button(self)['button label']

        print_assertion_to_console('my progress button', get_patient_tools_button, button_label_assertion)

        self.assertEqual(get_patient_tools_button, button_label_assertion)

    def test_patient_tools_button_click(self):

        PatientNavBar.click_patient_tools_button()

        page_status_code = CommonPageObject.get_page_response(self)

        self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

        page_url = CommonPageObject.get_page_url(self)

        self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'dashboard_bp.user_tools'))

    def test_patient_logout_button_label(self):
        button_label_assertion = "Log Out"

        get_logout_button = PatientNavBar.get_logout_button(self)['button label']

        print_assertion_to_console('patient logout button', get_logout_button, button_label_assertion)

        self.assertEqual(get_logout_button, button_label_assertion)

    def test_patient_logout_button_click(self):

        PatientNavBar.click_logout_button()

        page_status_code = CommonPageObject.get_page_response(self)

        self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

        page_url = CommonPageObject.get_page_url(self)

        self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'auth_bp.logout'))

    def test_patient_settings_button_label(self):
        button_label_assertion = "Settings"

        get_settings_button = PatientNavBar.get_settings_button(self)['button label']

        print_assertion_to_console('patient settings button', get_settings_button, button_label_assertion)

        self.assertEqual(get_settings_button, button_label_assertion)

    def test_patient_settings_button_click(self):

        PatientNavBar.click_acc_settings_button()

        page_status_code = CommonPageObject.get_page_response(self)

        self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

        page_url = CommonPageObject.get_page_url(self)

        self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'acc_settings_bp.patient_acc_settings'))

    class TestPsychiatristNavBar(LiveServerTestCase):

        # Element Specific Tests ----------------------------------------------------

        def test_psychiatrist_dashboard_button_label(self):
            button_label_assertion = "Dashboard"

            get_psychiatrist_dashboard_button = PsychiatristNavBar.get_dashboard_button(self)['button label']

            print_assertion_to_console('psychiatrist dashboard button', get_psychiatrist_dashboard_button,
                                       button_label_assertion)

            self.assertEqual(get_psychiatrist_dashboard_button, button_label_assertion)

        def test_psychiatrist_dashboard_button_click(self):

            PsychiatristNavBar.click_dashboard_button()

            page_status_code = CommonPageObject.get_page_response(self)

            self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

            page_url = CommonPageObject.get_page_url(self)

            self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'dashboard_bp.dashboard'))

        def test_my_patients_button_label(self):
            button_label_assertion = "My Patients"

            get_my_patients_button = PsychiatristNavBar.get_my_patients_button(self)['button label']

            print_assertion_to_console('my patients button', get_my_patients_button, button_label_assertion)

            self.assertEqual(get_my_patients_button, button_label_assertion)

        def test_my_patients_button_click(self):
            PsychiatristNavBar.click_my_patients_button()

            page_status_code = CommonPageObject.get_page_response(self)

            self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

            page_url = CommonPageObject.get_page_url(self)

            self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'dashboard_bp.my_patients'))

        def test_psychiatrist_tools_button_label(self):
            button_label_assertion = "Patient Tools"

            get_patient_tools_button = PsychiatristNavBar.get_psychiatrist_tools_button(self)['button label']

            print_assertion_to_console('patient tools button', get_patient_tools_button, button_label_assertion)

            self.assertEqual(get_patient_tools_button, button_label_assertion)

        def test_psychiatrist_tools_button_click(self):
            PsychiatristNavBar.click_psychiatrist_tools_button()

            page_status_code = CommonPageObject.get_page_response(self)

            self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

            page_url = CommonPageObject.get_page_url(self)

            self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'dashboard_bp.psychiatrist_tools'))

        def test_psychiatrist_logout_button_label(self):
            button_label_assertion = "Log Out"

            get_logout_button = PsychiatristNavBar.get_logout_button(self)['button label']

            print_assertion_to_console('psychiatrist logout button', get_logout_button, button_label_assertion)

            self.assertEqual(get_logout_button, button_label_assertion)

        def test_psychiatrist_logout_button_click(self):

            PsychiatristNavBar.click_logout_button()

            page_status_code = CommonPageObject.get_page_response(self)

            self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

            page_url = CommonPageObject.get_page_url(self)

            self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'auth_bp.logout'))

        def test_psychiatrist_settings_button_label(self):
            button_label_assertion = "Settings"

            get_settings_button = PsychiatristNavBar.get_settings_button(self)['button label']

            print_assertion_to_console('psychiatrist settings button', get_settings_button, button_label_assertion)

            self.assertEqual(get_settings_button, button_label_assertion)

        def test_psychiatrist_settings_button_click(self):
            PsychiatristNavBar.click_acc_settings_button()

            page_status_code = CommonPageObject.get_page_response(self)

            self.assertEqual(page_status_code, 200)  # Our page status code should equal 200 if it is functional.

            page_url = CommonPageObject.get_page_url(self)

            self.assertTrue(compare_and_evaluate_relative_urls(page_url, 'acc_settings_bp.psychiatrist_acc_settings'))
