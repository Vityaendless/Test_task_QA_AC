from .pages.dropdown_page import DropdownPage
import pytest


@pytest.mark.needcheck
class TestSelectedFromDropdownPage():
    def test_user_can_select_option_from_dropdown(self, browser):
        """Test with selected option in dropdown"""
        link = "http://the-internet.herokuapp.com/dropdown"
        page = DropdownPage(browser, link)
        page.open()
        page.user_select_option()