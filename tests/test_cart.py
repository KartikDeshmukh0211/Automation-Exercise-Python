import time

from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage
from pages.signup_and_login_page import SignupAndLoginPage
from pages.view_cart_page import ViewCartPage
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader


class TestCart(BaseTest):
    def test_12_add_products_in_cart(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_products_button()
        product_page = ProductsPage(self.driver)

        product_page.hover_and_add_first_product()
        product_page.click_continue_shopping()

        product_page.hover_and_add_second_product()
        product_page.click_view_cart()

        view_cart_page = ViewCartPage(self.driver)
        requird_products = 2
        assert view_cart_page.get_products_count() == requird_products
        
        prices = view_cart_page.get_prices()
        quantities = view_cart_page.get_quantities()
        totals = view_cart_page.get_totals()
        
        # print(prices, quantities, totals) 
        # ['Rs. 500', 'Rs. 400'] ['1', '1'] ['Rs. 500', 'Rs. 400']
        
        assert len(prices) == requird_products
        assert len(quantities) == requird_products
        assert len(totals) == requird_products
        
    def test_13_verify_product_quantity_cart(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_third_view_product()
        product_details_page = ProductDetailsPage(self.driver)
        assert product_details_page.is_product_detail_visible()

        quantity = 4
        product_details_page.enter_quantity(quantity)     
        product_details_page.click_add_to_cart()
        product_details_page.click_view_cart()

        view_cart_page = ViewCartPage(self.driver)
        actual_quantity = view_cart_page.get_product_quantity()

        assert actual_quantity == quantity
        
    def test_17_remove_products_from_cart(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()
        products_page = ProductsPage(self.driver)
        
        products_page.hover_and_add_first_product()
        products_page.click_continue_shopping()

        home_page.click_cart_button()

        view_cart_page = ViewCartPage(self.driver)
        assert view_cart_page.is_cart_page_visible()

        view_cart_page.clilck_remove_product_button()
        time.sleep(3)
        assert view_cart_page.is_cart_empty()
        
    def test_20_search_products_and_verify_cart_after_login(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()
        products_page = ProductsPage(self.driver)
        assert products_page.is_all_products_page_visible()

        search_item = "Jeans"
        products_page.enter_product_in_search_field(search_item)
        products_page.click_search_button()

        assert products_page.is_search_product_text_present()

        product_names = products_page.get_searched_product_names()
        # print(product_names)
        
        for name in product_names:
            assert search_item.lower() in name.lower()

        products_page.add_all_products_to_cart()

        home_page.click_cart_button()
        view_cart_page = ViewCartPage(self.driver)

        cart_products_before_login = view_cart_page.get_product_names()
        assert len(cart_products_before_login) > 0

        home_page.click_sigup_and_login_button()
        login_page = SignupAndLoginPage(self.driver)

        config = ConfigReader()

        login_page.enter_email_in_login_field(config.get_email())
        login_page.enter_password_in_login_field(config.get_password())
        login_page.click_login_button()

        home_page.click_cart_button()

        cart_products_after_login = view_cart_page.get_product_names()

        assert cart_products_before_login == cart_products_after_login
        
    def test_22_add_to_cart_from_recommended_items(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.scroll_to_bottom()
        assert home_page.is_recommended_items_visible()

        product_name = "Blue Top"
        home_page.add_first_recommended_product_to_cart()
        home_page.click_view_cart_button()
        
        view_cart_page = ViewCartPage(self.driver)
        cart_products = view_cart_page.get_product_names()

        assert product_name in cart_products