from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.XPATH, '//*[@id="searchInput"]')
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search-form"]/fieldset/button')
    RESULTS = (By.XPATH, '//*[@id="mw-content-text"]')
