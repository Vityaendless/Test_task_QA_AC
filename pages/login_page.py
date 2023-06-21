from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """Tests for page after success authorization"""
    def shold_be_success_message(self):
        """Checking if success message is exists"""
        assert self.is_element_present(*LoginPageLocators.SUCCESS_MESSAGE), "Success area is not presented"