from .base_page import BasePage
from .locators import FiledownloadPageLocators
import urllib.request


def download(fromlink, path):
    """Download file function"""
    urllib.request.urlretrieve(fromlink, path)


class FiledownloadPage(BasePage):
    """Tests for file download page"""
    def should_be_link(self):
        """Checking if link is exists"""
        assert self.is_element_present(*FiledownloadPageLocators.LINK), "Link is not presented"

    def user_download(self, destination):
        """Checking file downloading"""
        self.should_be_link()
        file = self.browser.find_element(*FiledownloadPageLocators.LINK)
        url = file.get_attribute("href")
        download(url, destination)
        with open('file.txt') as f:
            lines = f.readlines()
        assert lines[0] == "test 123", "Information in file is different"