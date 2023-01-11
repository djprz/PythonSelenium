from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import SearchPageLocators
from selenium.webdriver.support.ui import Select
import time


class SearchPage(BasePage):

    def __init__(self, driver, wait):
        self.url = "https://wikipedia.org/"
        self.locator = SearchPageLocators
        super().__init__(driver, wait)

    def go_to_search_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        assert self.get_title() == title

    def make_a_search(self, input_text):
        # Send values to search using locator SEARCH_INPUT
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(input_text)
        # Click on search button with locator SEARCH_BUTTON
        self.driver.find_element(*self.locator.SEARCH_BUTTON).click()
        # wait until element with locator SEARCH_BUTTON is present
        self.wait.until(EC.presence_of_element_located(self.locator.RESULTS))

    def select_option_dropdown(self, search_option):
        self.driver.find_element(*self.locator.SEARCH_INPUT).send_keys(search_option)
        # wait until element with locator SEARCH_DROPDOWN_OPTIONS is present
        self.wait.until(EC.presence_of_element_located(self.locator.SEARCH_DROPDOWN_OPTIONS))
        drop = self.driver.find_element(*self.locator.SEARCH_DROPDOWN_OPTIONS)
        # To complete how to click on <a> link element using href.
