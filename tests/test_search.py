# coding=utf-8
import pytest
from pages.search_page import SearchPage
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = SearchPage(self.driver, self.wait)
        self.page.go_to_search_page()

    def test_title(self, load_pages):
        self.page.check_title("Wikipedia")

    def test_search(self, load_pages):
        self.page.make_a_search("Selenium")

    def test_search_dropdown(self, load_pages):
        self.page.select_option_dropdown("Selenio")
