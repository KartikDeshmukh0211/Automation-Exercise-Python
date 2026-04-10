from pages.home_page import HomePage
from pages.test_cases_page import TestCasesPage
from tests.base_test import BaseTest


class TestNavigation(BaseTest):
    def test_07_verify_test_cases_page(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_test_cases_button()

        test_cases_page = TestCasesPage(self.driver)
        expected_text = "TEST CASES"

        assert test_cases_page.get_test_cases_text() == expected_text
        
    