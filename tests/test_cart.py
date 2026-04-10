from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage
from pages.view_cart_page import ViewCartPage
from tests.base_test import BaseTest


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