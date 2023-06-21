from selenium.common.exceptions import NoSuchElementException as NSEE


"""Base class"""
class BasePage():
    def __init__(self, browser, url, timeout=10):
        """Initialization"""
        self.browser = browser
        self.url = url

    def is_element_present(self, how, what):
        """Checking if the element exists"""
        try:
            self.browser.find_element(how,what)
        except NSEE:
            return False
        return True

    def open(self):
        """Opening the page"""
        self.browser.get(self.url)

    def input_information(self, information, searching_type, info_for_finding):
        """Inputing information in area"""
        area = self.browser.find_element(searching_type, info_for_finding)
        area.send_keys(information)
        return area