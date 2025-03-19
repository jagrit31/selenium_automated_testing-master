from selenium.webdriver.common.by import By
from values import strings
from .basescreen import BaseScreen


class ServicesPage(BaseScreen):
    """Models login functionality as a Page Object"""

    logo = (By.CLASS_NAME, "tb-logo")
    # newly added
    first_service_section = (By.CSS_SELECTOR, "div.tb-service-selector-item:first-child")
    category_box = (By.CSS_SELECTOR, "div.tb-category-box:first-child")
    service_selector = (By.CSS_SELECTOR, "div.tb-dropdown-toggle.no-selection")
    service = (By.CSS_SELECTOR, "ul.tb-dropdown-menu>li:first-child")
    submit_button = (By.CSS_SELECTOR, "button.tb-button")
    # sms validation
    phone_number_input = (By.ID, "input")
    sms_code_fields = (By.CSS_SELECTOR, "div.tb-input-container.noselect>input")
    # verify on profile page
    first_name = (By.CSS_SELECTOR, "span.first-name")
    last_name = (By.CSS_SELECTOR, "span.last-name")
    # error div
    error_div = (By.CSS_SELECTOR, "div.tb-error-message")

    def logo_is_displayed(self):
        logo = self.select_element(self.logo)
        assert logo.is_displayed(), "Logo is missing."

    # newly added
    def choose_service_type(self):
        element = self.select_element(self.first_service_section)
        self.mouse_hover(element)
        element.click()

    def choose_category(self):
        random_box = self.hover_one_of_elements(self.category_box)
        random_box.click()

    def choose_service(self):
        self.select_element(self.service_selector).click()
        self.select_element(self.service).click()
        self.wait_until_clickable(self.submit_button).click()

    def input_mobile_num(self, mobile_num):
        number_field = self.select_element(self.phone_number_input)
        number_field.send_keys(mobile_num)
        self.wait_until_clickable(self.submit_button).click()
        pass

    def input_sms_code(self, sms_code):
        sms_code_fields = self.select_elements(self.sms_code_fields)
        assert len(sms_code_fields) == len(sms_code), "Number of SMS code digits is incorrect"
        for i, field in enumerate(sms_code_fields):
            sms_code_fields[i].send_keys(sms_code[i])
        self.wait_until_clickable(self.submit_button).click()

    def validate_correct_name_is_displayed(self):
        first_name = self.select_element(self.first_name).text
        last_name = self.select_element(self.last_name).text
        assert first_name.lower() == strings.first_name.lower(), "Incorrect first name"
        assert last_name.lower() == strings.last_name.lower(), "Incorrect last name"

    def validate_error_message_is_displayed(self):
        error_msg_is_displayed = self.is_element_visible(self.error_div)
        assert error_msg_is_displayed, "Validation error message is not displayed."