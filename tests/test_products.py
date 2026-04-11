from pages.brand_products_page import BrandProductsPage
from pages.category_products_page import CategoryProductsPage
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage
from tests.base_test import BaseTest
from utils.data_generator import *


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
        
    def test_18_view_category_product(self):
        home_page = HomePage(self.driver)
        assert home_page.is_category_sidebar_visible()

        home_page.click_women_category()
        home_page.click_women_dress()

        category_products_page = CategoryProductsPage(self.driver)
        assert "WOMEN - DRESS PRODUCTS" == category_products_page.get_category_title_text()
        
        home_page.click_men_category()
        home_page.click_men_jeans()

        assert "MEN - JEANS PRODUCTS" == category_products_page.get_category_title_text()
        
    def test_19_view_and_cart_brand_products(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()
        products_page = ProductsPage(self.driver)

        assert products_page.is_brands_sidebar_visible()
        products_page.click_brand("Polo")

        brand_page = BrandProductsPage(self.driver)
        assert "POLO PRODUCTS" in brand_page.get_brand_title_text()
        assert brand_page.is_products_visible()

        products_page.click_brand("H&M")

        assert "H&M PRODUCTS" in brand_page.get_brand_title_text()
        assert brand_page.is_products_visible()
        
    def test_21_add_review_on_product(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()

        products_page = ProductsPage(self.driver)
        assert products_page.is_all_products_page_visible()

        products_page.click_first_product_view_button()

        product_details_page = ProductDetailsPage(self.driver)

        assert product_details_page.is_review_section_visible()

        name = generate_random_name()
        email = generate_random_email()
        review = generate_random_string(20)

        product_details_page.enter_review_name(name)
        product_details_page.enter_review_email(email)
        product_details_page.enter_review_text(review)

        product_details_page.click_submit_review()

        assert product_details_page.get_review_success_message() == "Thank you for your review."