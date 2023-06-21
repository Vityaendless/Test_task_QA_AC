from .pages.formauth_page import FormauthPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.needcheck
class TestAuthFromFormauthPage():
    def test_guest_can_try_to_auth_in_page(self, browser):
        """Test with checked authorization through the form"""
        link = "http://the-internet.herokuapp.com/login"
        page = FormauthPage(browser, link)
        page.open()
        user_login = "tomsmith"
        user_password = "SuperSecretPassword!"
        page.user_should_auth(user_login, user_password)
        login_page = LoginPage(browser, browser.current_url)
        login_page.shold_be_success_message()
