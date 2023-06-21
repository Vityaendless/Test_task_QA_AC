from .base_page import BasePage
from .locators import KeypressesPageLocators


class KeypressesPage(BasePage):
    """Tests for keypress page"""
    def should_be_input_area(self):
        """Checking if input area is exists"""
        assert self.is_element_present(*KeypressesPageLocators.INPUT_AREA), "Input area is not presented"

    def should_be_result_area(self):
        """Checking if result area is exists"""
        assert self.is_element_present(*KeypressesPageLocators.RESULT_AREA), "Result area is not clicked"

    def user_input_key(self, str):
        """Checking if keypressed symbol equal to output symbol"""
        self.should_be_input_area()
        self.should_be_result_area()
        input_area = self.input_information(str, *KeypressesPageLocators.INPUT_AREA)
        value_in_input = input_area.get_attribute("value")
        last_key = value_in_input[-1].capitalize()
        result_area = self.browser.find_element(*KeypressesPageLocators.RESULT_AREA)
        text_in_result_area = result_area.text
        assert last_key == text_in_result_area[-1], "Symbols are not equals"