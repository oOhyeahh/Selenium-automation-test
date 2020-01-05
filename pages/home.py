from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class WelcomePage:
    URL = 'http://newtours.demoaut.com/mercurywelcome.php'
    USERNAME_INPUT = (By.NAME, 'userName')
    PASSWORD_INPUT = (By.NAME, 'password')
    LOGIN = (By.NAME, 'login')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        """A function to start the webdriver
        """
        self.browser.get(self.URL)

    def login(self, username: str, password: str) -> None:
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(username)
        password_input = self.browser.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(password)
        login_button = self.browser.find_element(*self.LOGIN)
        login_button.send_keys(Keys.RETURN)

