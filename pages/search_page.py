from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import SearchPageLocators
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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
        
        # Click on search button with locator SEARCH_BUTTON
  
        # wait until element with locator RESULTS is present
        pass


    def select_option_dropdown(self, search_option):
        # Find element with locator SEARCH_INPUT and send 'search_option' string

        # Wait until element with locator SEARCH_DROPDOWN_OPTIONS is present

        # Select first option from dropdown and click it
        pass