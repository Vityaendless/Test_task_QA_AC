from .pages.filedownload_page import FiledownloadPage
import pytest


@pytest.mark.needcheck
class TestFiledownload():
    def test_user_download_file(self, browser):
        """Test with a downloaded file and checking the text in it"""
        link = "http://the-internet.herokuapp.com/download"
        page = FiledownloadPage(browser, link)
        page.open()
        download_to_this_file = 'file.txt'
        page.user_download(download_to_this_file)