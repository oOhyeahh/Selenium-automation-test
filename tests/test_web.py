import pytest

from pages.home import WelcomePage
from pages.flight_details import FlightFinderPage
from pages.flight_selection import FlightSelection
from pages.flight_booking import FlightBookingPage

from selenium.webdriver import Chrome


@pytest.fixture
def browser():
    # Initialize ChromeDriver
    driver = Chrome()

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_login(browser):
    # Set up test case data
    username = 'mercury'
    password = 'mercury'
    firstname = 'firstname'
    lastname = 'lastname'
    card_number = '348435353480634'


    # login with username and password
    welcome_page = WelcomePage(browser)
    welcome_page.load()
    welcome_page.login(username, password)

    # enter the flight details in Flight Finder Page
    details_page = FlightFinderPage(browser)
    details_page.select_one_way_flight()
    details_page.select_departure_location('Sydney')
    details_page.select_destination_location('London')
    details_page.select_first_class_service()
    details_page.continue_booking_process()

    # reserve the flight 

    selection_page = FlightSelection(browser)
    selection_page.process_reservation()   

    # book the flight

    booking_page = FlightBookingPage(browser)
    booking_page.enter_first_name(firstname)
    booking_page.enter_last_name(lastname)
    booking_page.enter_card_number(card_number)
    booking_page.select_ticketless_travel()
    booking_page.process_secure_purchase()

    

