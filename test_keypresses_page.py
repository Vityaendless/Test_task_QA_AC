from .pages.keypresses_page import KeypressesPage
import pytest


@pytest.mark.needcheck
class TestPressKey():
    def test_user_can_see_inputed_symbol(self, browser):
        """Test with checked input keypress"""
        link = "http://the-internet.herokuapp.com/key_presses"
        page = KeypressesPage(browser, link)
        page.open()
        page.user_input_key("n")