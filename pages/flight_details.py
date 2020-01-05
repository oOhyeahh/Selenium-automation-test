from selenium.webdriver.common.by import By


class FlightFinderPage:
    ONE_WAY_FLIGHT = (
        By.CSS_SELECTOR, 'font:nth-child(1) > input:nth-child(2)')
    DEPARTURE_LOCATION = (By.NAME, 'fromPort')
    DESTINATION_LOCATION = (By.NAME, 'toPort')
    FIRST_CLASS_SERVICE = (By.NAME, 'servClass')
    CONTINUE = (By.NAME, 'findFlights')

    def __init__(self, browser):
        self.browser = browser

    def select_one_way_flight(self) -> None:
        self.browser.find_element(*self.ONE_WAY_FLIGHT).click()

    def select_departure_location(self, location) -> None:
        departure_location = self.browser.find_element(
            *self.DEPARTURE_LOCATION)
        departure_location.send_keys(location)

    def select_destination_location(self, location) -> None:
        destination_location = self.browser.find_element(
            *self.DESTINATION_LOCATION)
        destination_location.send_keys(location)

    def select_first_class_service(self) -> None:
        self.browser.find_elements(*self.FIRST_CLASS_SERVICE)[2].click()

    def continue_booking_process(self) -> None:
        """click the continue button and process to next page
        """
        self.browser.find_element(*self.CONTINUE).click()
