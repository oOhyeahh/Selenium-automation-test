from selenium.webdriver.common.by import By


class FlightSelection:
    CONTINUE = (By.NAME, 'reserveFlights')

    def __init__(self, browser):
        self.browser = browser

    def process_reservation(self) -> None:
        """click the continue button and process the flight reservation
        """
        self.browser.find_element(*self.CONTINUE).click()
