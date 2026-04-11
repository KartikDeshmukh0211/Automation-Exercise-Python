import pytest

from pages.home_page import HomePage
from pages.test_cases_page import TestCasesPage
from tests.base_test import BaseTest


class TestNavigation(BaseTest):
    @pytest.mark.regression
    @pytest.mark.ui
    def test_07_verify_test_cases_page(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_test_cases_button()

        test_cases_page = TestCasesPage(self.driver)
        expected_text = "TEST CASES"

        assert test_cases_page.get_test_cases_text() == expected_text
    
    @pytest.mark.regression
    @pytest.mark.ui    
    def test_25_verify_scroll_up_using_arrow_button_and_scroll_down_functionality(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.scroll_to_bottom()
        assert home_page.is_subscription_text_visible()

        home_page.click_scroll_up_arrow()
        assert home_page.is_top_text_visible()
    
    @pytest.mark.regression
    @pytest.mark.ui    
    def test_26_verify_scroll_up_without_arrow_button_and_scroll_down_functionality(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.scroll_to_bottom()
        assert home_page.is_subscription_text_visible()

        home_page.scroll_to_top()
        assert home_page.is_top_text_visible()
    