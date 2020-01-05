from selenium.webdriver.common.by import By


class FlightBookingPage:
    FIRST_NAME_INPUT = (By.NAME, 'passFirst0')
    LAST_NAME_INPUT = (By.NAME, 'passLast0')
    CARD_NUMBER_INPUT = (By.NAME, 'creditnumber')
    TICKETLESS = (By.NAME, 'ticketLess')
    SECURE_PURCHASE = (By.NAME, 'buyFlights')

    def __init__(self, browser):
        self.browser = browser

    def enter_first_name(self, firstname: str) -> None:
        firstname_input = self.browser.find_element(*self.FIRST_NAME_INPUT)
        firstname_input.send_keys(firstname)

    def enter_last_name(self, lastname: str) -> None:
        lastname_input = self.browser.find_element(*self.LAST_NAME_INPUT)
        lastname_input.send_keys(lastname)

    def enter_card_number(self, card_number: str) -> None:
        card_number_input = self.browser.find_element(*self.CARD_NUMBER_INPUT)
        card_number_input.send_keys(card_number)

    def select_ticketless_travel(self) -> None:
        self.browser.find_element(*self.TICKETLESS).click()

    def process_secure_purchase(self) -> None:
        self.browser.find_element(*self.SECURE_PURCHASE).click()
