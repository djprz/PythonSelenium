from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_INPUT = (By.ID, "searchInput")
    SEARCH_BUTTON = (By.XPATH, '//*[@id="search-form"]/fieldset/button')
    SEARCH_DROPDOWN_OPTIONS = (By.XPATH, '//*[@id="typeahead-suggestions"]/div')
    SUGGESTION_TITLE = (By.XPATH, "//h3[contains(text(), {})")
    RESULTS = (By.XPATH, '//*[@id="mw-content-text"]')
