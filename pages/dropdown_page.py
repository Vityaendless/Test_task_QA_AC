from .base_page import BasePage
from .locators import DropdownPageLocators

class DropdownPage(BasePage):
    """Dropdown page tests"""
    def should_be_select_area(self):
        """Checking if select is exists"""
        assert self.is_element_present(*DropdownPageLocators.SELECT_AREA), "Select area is not presented"

    def should_be_clicked_option(self):
        """Checking if option is exists"""
        assert self.is_element_present(*DropdownPageLocators.CHECK_OPTION), "Option in select is not clicked"

    def user_select_option(self):
        """Checking that option is checked"""
        self.should_be_select_area()
        self.should_be_clicked_option()
        selected_option = self.browser.find_element(*DropdownPageLocators.CHECK_OPTION)
        selected_option.click()
        is_checked = selected_option.get_attribute("checked")
        assert is_checked is not None, "Option is not selected"