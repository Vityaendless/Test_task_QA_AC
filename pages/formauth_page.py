from .base_page import BasePage
from .locators import FormauthPageLocators

class FormauthPage(BasePage):
    """Tests for authorization form"""
    def should_be_user_area(self):
        """Checking if user area is exists"""
        assert self.is_element_present(*FormauthPageLocators.USER_AREA), "User area is not presented"

    def should_be_password_area(self):
        """Checking if password area is exists"""
        assert self.is_element_present(*FormauthPageLocators.PASSWORD_AREA), "Password area is not presented"

    def should_be_login_button(self):
        """Checking if login button is exists"""
        assert self.is_element_present(*FormauthPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def is_auth_form_presented(self):
        """Checking if auth form is exists"""
        self.should_be_user_area()
        self.should_be_password_area()
        self.should_be_login_button()

    def go_to_login_page(self):
        """Checking that the redirect to the success page is happened"""
        login_button = self.browser.find_element(*FormauthPageLocators.LOGIN_BUTTON)
        login_button.click()

    def user_should_auth(self, user, password):
        """Checking that user could authorization"""
        self.is_auth_form_presented()
        user_area = self.input_information(user, *FormauthPageLocators.USER_AREA)
        password_area = self.input_information(password, *FormauthPageLocators.PASSWORD_AREA)
        self.go_to_login_page()

