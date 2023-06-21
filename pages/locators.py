from selenium.webdriver.common.by import By


class FormauthPageLocators():
    """Locators for authrorization form"""
    USER_AREA = (By.CSS_SELECTOR,"input#username")
    PASSWORD_AREA = (By.CSS_SELECTOR, "input#password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")

class LoginPageLocators():
    """Locatos for success authorization page"""
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.flash.success")

class DropdownPageLocators():
    """Locators for dropdown page"""
    SELECT_AREA = (By.CSS_SELECTOR, "select#dropdown")
    CHECK_OPTION = (By.CSS_SELECTOR, "option:nth-child(2)")

class KeypressesPageLocators():
    """Locators for keypress page"""
    INPUT_AREA = (By.CSS_SELECTOR, "input#target")
    RESULT_AREA = (By.CSS_SELECTOR, "p#result")

class FiledownloadPageLocators():
    """Locators for download file page"""
    LINK = (By.LINK_TEXT, "test.txt")