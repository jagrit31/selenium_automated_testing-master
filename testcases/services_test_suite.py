import unittest
from webdriver import Driver
from values import strings
from pageobjects.servicespage import ServicesPage


class TestTechBuddyLogin(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    def test_logo_and_title_are_displayed(self):
        page = ServicesPage(self.driver)
        page.page_title_equals_to(strings.services_page_title)
        page.logo_is_displayed()

    def test_choose_a_service_correct_mobile_and_sms_code(self):
        page = ServicesPage(self.driver)
        page.choose_service_type()
        page.choose_category()
        page.choose_service()
        page.input_mobile_num(strings.correct_mobile_number)
        page.input_sms_code(strings.correct_sms_code)
        page.validate_correct_name_is_displayed()

    def test_choose_a_service_incorrect_mobile(self):
        page = ServicesPage(self.driver)
        page.choose_service_type()
        page.choose_category()
        page.choose_service()
        page.input_mobile_num(strings.incorrect_mobile_number_digits)
        page.validate_error_message_is_displayed()

    def test_choose_a_service_correct_mobile_incorrect_sms_code(self):
        page = ServicesPage(self.driver)
        page.choose_service_type()
        page.choose_category()
        page.choose_service()
        page.input_mobile_num(strings.correct_mobile_number)
        page.input_sms_code(strings.incorrect_sms_code)
        page.validate_error_message_is_displayed()

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == "__main__":
    unittest.main()