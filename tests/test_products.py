from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage
from tests.base_test import BaseTest


class TestProducts(BaseTest):
    def test_08_verify_all_products_and_product_details_page(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()
        
        products_page = ProductsPage(self.driver)
        assert products_page.is_all_products_page_visible()
        
        assert products_page.is_product_list_present()
        
        products_page.click_first_product_view_button()

        product_details_page = ProductDetailsPage(self.driver)
        assert product_details_page.is_product_name_present()
        assert product_details_page.is_category_visible()
        assert product_details_page.is_price_visible()
        assert product_details_page.is_availability_visible()
        assert product_details_page.is_conditon_visible()
        assert product_details_page.is_brand_visible()

    def test_09_search_product(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()
        
        products_page = ProductsPage(self.driver)
        assert products_page.is_all_products_page_visible()
        
        product_name = "Tshirt"
        products_page.enter_product_in_search_field(product_name)
        products_page.click_search_button()
        
        assert products_page.is_search_product_text_present()