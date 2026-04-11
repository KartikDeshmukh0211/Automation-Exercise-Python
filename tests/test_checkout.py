import os
import pytest

from pages import home_page
from pages.account_created_page import AccountCreatedPage
from pages.checkout_page import CheckoutPage
from pages.delete_account_page import DeleteAccountPage
from pages.home_page import HomePage
from pages.payment_done_page import PaymentDonePage
from pages.payment_page import PaymentPage
from pages.products_page import ProductsPage
from pages.signup_and_login_page import SignupAndLoginPage
from pages.signup_page import SignupPage
from pages.view_cart_page import ViewCartPage
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader
from utils.data_generator import *
from utils.file_utils import is_file_downloaded


class TestCheckout(BaseTest):
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_14_place_order_register_while_checkout(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()
        
        products_page = ProductsPage(self.driver)
        products_page.hover_and_add_first_product()
        products_page.click_continue_shopping()
        products_page.hover_and_add_second_product()
        products_page.click_continue_shopping()

        home_page.click_cart_button()
        view_cart_page = ViewCartPage(self.driver)
        assert view_cart_page.is_cart_page_visible()

        view_cart_page.click_checkout_button()
        view_cart_page.click_register_login_button()

        # filling details in signup page
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_signup_section_present()
        
        name = generate_random_name()
        email = generate_random_email()
        signup_and_login_page.enter_name_in_signup_field(name)
        signup_and_login_page.enter_email_in_signup_field(email)
        signup_and_login_page.click_signup_button()
        
        password = generate_random_password()
        first_name = generate_random_name()
        last_name = generate_random_name()
        company = generate_random_name()
        address1 = generate_random_address()
        address2 = generate_random_address()
        state = generate_random_name()
        city = generate_random_name()
        zipcode = generate_random_phone(6)
        mobile = generate_random_phone()
        
        signup_page = SignupPage(self.driver)
        signup_page.select_title("Mr")
        signup_page.enter_password(password)
        signup_page.select_day(21)
        signup_page.select_month("May")
        signup_page.select_year(2018)
        signup_page.select_newsletter()
        signup_page.select_offers()
        signup_page.enter_first_name(first_name)
        signup_page.enter_last_name(last_name)
        signup_page.enter_company(company)
        signup_page.enter_address1(address1)
        signup_page.enter_address2(address2)
        signup_page.enter_country("India")
        signup_page.enter_state(state)
        signup_page.enter_city(city)
        signup_page.enter_zipcode(zipcode)
        signup_page.enter_mobile(mobile)
        signup_page.click_create_account_button()

        account_created_page = AccountCreatedPage(self.driver)
        assert account_created_page.get_account_created_message() == "ACCOUNT CREATED!"
        
        account_created_page.click_continue_button()

        assert home_page.is_logged_in_as_username_present()
        home_page.click_cart_button()
        view_cart_page.click_checkout_button()
        
        checkout_page = CheckoutPage(self.driver)
        
        assert first_name in checkout_page.get_delivery_name()
        assert address1 in checkout_page.get_delivery_address()
        
        product_names = checkout_page.get_product_names()
        prices = checkout_page.get_product_prices()
        quantities = checkout_page.get_product_quantities()
        totals = checkout_page.get_product_totals()
        
        assert len(product_names) > 0
        assert len(prices) == len(product_names)
        assert len(quantities) == len(product_names)
        assert len(totals) == len(product_names)
                
        message = generate_random_string(12)
        checkout_page.enter_message(message)

        checkout_page.click_place_order_button()

        payment_page = PaymentPage(self.driver)
        assert payment_page.is_payment_page_visible()

        card_holder_name = generate_random_name()
        card_number = generate_random_phone(12)
        cvc = generate_random_phone(3)
        expiration_month = "January"
        expiration_year = 2016
        
        payment_page.enter_name_on_card(card_holder_name)
        payment_page.enter_card_number(card_number)
        payment_page.enter_CVC(cvc)
        payment_page.enter_expiration_month(expiration_month)
        payment_page.enter_expiration_year(expiration_year)
        payment_page.click_confirm_order_button()
        
        payment_done_page = PaymentDonePage(self.driver)
        expected_text1 = "ORDER PLACED!"
        
        assert payment_done_page.get_message() == expected_text1
        payment_done_page.click_continue_button()

        home_page.click_delete_account_button()

        delete_account_page = DeleteAccountPage(self.driver)
        expected_text2 = "ACCOUNT DELETED!"
        assert delete_account_page.get_account_deleted_message() == expected_text2

        delete_account_page.click_contine_button()

        assert home_page.is_app_logo_present()
    
    
    @pytest.mark.regression
    @pytest.mark.checkout    
    def test_15_place_order_register_before_checkout(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        
        # filling details in signup page
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_signup_section_present()
        
        name = generate_random_name()
        email = generate_random_email()
        signup_and_login_page.enter_name_in_signup_field(name)
        signup_and_login_page.enter_email_in_signup_field(email)
        signup_and_login_page.click_signup_button()
        
        password = generate_random_password()
        first_name = generate_random_name()
        last_name = generate_random_name()
        company = generate_random_name()
        address1 = generate_random_address()
        address2 = generate_random_address()
        state = generate_random_name()
        city = generate_random_name()
        zipcode = generate_random_phone(6)
        mobile = generate_random_phone()
        
        signup_page = SignupPage(self.driver)
        signup_page.select_title("Mr")
        signup_page.enter_password(password)
        signup_page.select_day(21)
        signup_page.select_month("May")
        signup_page.select_year(2018)
        signup_page.select_newsletter()
        signup_page.select_offers()
        signup_page.enter_first_name(first_name)
        signup_page.enter_last_name(last_name)
        signup_page.enter_company(company)
        signup_page.enter_address1(address1)
        signup_page.enter_address2(address2)
        signup_page.enter_country("India")
        signup_page.enter_state(state)
        signup_page.enter_city(city)
        signup_page.enter_zipcode(zipcode)
        signup_page.enter_mobile(mobile)
        signup_page.click_create_account_button()

        account_created_page = AccountCreatedPage(self.driver)
        assert account_created_page.get_account_created_message() == "ACCOUNT CREATED!"
        
        account_created_page.click_continue_button()

        assert home_page.is_logged_in_as_username_present()

        home_page.click_products_button()
        
        products_page = ProductsPage(self.driver)
        products_page.hover_and_add_first_product()
        products_page.click_continue_shopping()
        products_page.hover_and_add_second_product()
        products_page.click_continue_shopping()

        home_page.click_cart_button()
        view_cart_page = ViewCartPage(self.driver)
        assert view_cart_page.is_cart_page_visible()

        view_cart_page.click_checkout_button()
        
        checkout_page = CheckoutPage(self.driver)
        
        assert first_name in checkout_page.get_delivery_name()
        assert address1 in checkout_page.get_delivery_address()
        
        product_names = checkout_page.get_product_names()
        prices = checkout_page.get_product_prices()
        quantities = checkout_page.get_product_quantities()
        totals = checkout_page.get_product_totals()
        
        assert len(product_names) > 0
        assert len(prices) == len(product_names)
        assert len(quantities) == len(product_names)
        assert len(totals) == len(product_names)
                
        message = generate_random_string(12)
        checkout_page.enter_message(message)

        checkout_page.click_place_order_button()

        payment_page = PaymentPage(self.driver)
        assert payment_page.is_payment_page_visible()

        card_holder_name = generate_random_name()
        card_number = generate_random_phone(12)
        cvc = generate_random_phone(3)
        expiration_month = "January"
        expiration_year = 2016
        
        payment_page.enter_name_on_card(card_holder_name)
        payment_page.enter_card_number(card_number)
        payment_page.enter_CVC(cvc)
        payment_page.enter_expiration_month(expiration_month)
        payment_page.enter_expiration_year(expiration_year)
        payment_page.click_confirm_order_button()
        
        payment_done_page = PaymentDonePage(self.driver)
        expected_text1 = "ORDER PLACED!"
        
        assert payment_done_page.get_message() == expected_text1
        payment_done_page.click_continue_button()

        home_page.click_delete_account_button()

        delete_account_page = DeleteAccountPage(self.driver)
        expected_text2 = "ACCOUNT DELETED!"
        assert delete_account_page.get_account_deleted_message() == expected_text2

        delete_account_page.click_contine_button()

        assert home_page.is_app_logo_present()
        
    
    @pytest.mark.regression
    @pytest.mark.smoke
    @pytest.mark.checkout
    def test_16_place_order_login_before_checkout(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_sigup_and_login_button()

        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_login_section_present()
        
        config = ConfigReader()
        email = config.get_email()
        password = config.get_password()
        
        signup_and_login_page.enter_email_in_login_field(email)
        signup_and_login_page.enter_password_in_login_field(password)
        signup_and_login_page.click_login_button()
        
        assert home_page.is_logged_in_as_username_present()
        
        home_page.click_products_button()
        
        products_page = ProductsPage(self.driver)
        products_page.hover_and_add_first_product()
        products_page.click_continue_shopping()
        products_page.hover_and_add_second_product()
        products_page.click_continue_shopping()

        home_page.click_cart_button()
        view_cart_page = ViewCartPage(self.driver)
        assert view_cart_page.is_cart_page_visible()

        view_cart_page.click_checkout_button()
        
        checkout_page = CheckoutPage(self.driver)
        
        first_name = config.get_first_name()
        address1 = config.get_address1()

        assert first_name in checkout_page.get_delivery_name()
        assert address1 in checkout_page.get_delivery_address()
        
        product_names = checkout_page.get_product_names()
        prices = checkout_page.get_product_prices()
        quantities = checkout_page.get_product_quantities()
        totals = checkout_page.get_product_totals()
        
        assert len(product_names) > 0
        assert len(prices) == len(product_names)
        assert len(quantities) == len(product_names)
        assert len(totals) == len(product_names)
                
        message = generate_random_string(12)
        checkout_page.enter_message(message)

        checkout_page.click_place_order_button()

        payment_page = PaymentPage(self.driver)
        assert payment_page.is_payment_page_visible()

        card_holder_name = generate_random_name()
        card_number = generate_random_phone(12)
        cvc = generate_random_phone(3)
        expiration_month = "January"
        expiration_year = 2016
        
        payment_page.enter_name_on_card(card_holder_name)
        payment_page.enter_card_number(card_number)
        payment_page.enter_CVC(cvc)
        payment_page.enter_expiration_month(expiration_month)
        payment_page.enter_expiration_year(expiration_year)
        payment_page.click_confirm_order_button()
        
        payment_done_page = PaymentDonePage(self.driver)
        expected_text1 = "ORDER PLACED!"
        
        assert payment_done_page.get_message() == expected_text1
        payment_done_page.click_continue_button()

        # we will avoid deleting the account during login steps inorder to preserve the account details...
        assert home_page.is_app_logo_present()
    
    @pytest.mark.regression
    @pytest.mark.checkout     
    def test_23_verify_address_details_in_checkout_page(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        
        # filling details in signup page
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_signup_section_present()
        
        name = generate_random_name()
        email = generate_random_email()
        signup_and_login_page.enter_name_in_signup_field(name)
        signup_and_login_page.enter_email_in_signup_field(email)
        signup_and_login_page.click_signup_button()
        
        password = generate_random_password()
        first_name = generate_random_name()
        last_name = generate_random_name()
        company = generate_random_name()
        address1 = generate_random_address()
        address2 = generate_random_address()
        state = generate_random_name()
        city = generate_random_name()
        zipcode = generate_random_phone(6)
        mobile = generate_random_phone()
        
        signup_page = SignupPage(self.driver)
        signup_page.select_title("Mr")
        signup_page.enter_password(password)
        signup_page.select_day(21)
        signup_page.select_month("May")
        signup_page.select_year(2018)
        signup_page.select_newsletter()
        signup_page.select_offers()
        signup_page.enter_first_name(first_name)
        signup_page.enter_last_name(last_name)
        signup_page.enter_company(company)
        signup_page.enter_address1(address1)
        signup_page.enter_address2(address2)
        signup_page.enter_country("India")
        signup_page.enter_state(state)
        signup_page.enter_city(city)
        signup_page.enter_zipcode(zipcode)
        signup_page.enter_mobile(mobile)
        signup_page.click_create_account_button()

        account_created_page = AccountCreatedPage(self.driver)
        assert account_created_page.get_account_created_message() == "ACCOUNT CREATED!"
        
        account_created_page.click_continue_button()

        assert home_page.is_logged_in_as_username_present()

        home_page.click_products_button()
        
        products_page = ProductsPage(self.driver)
        products_page.hover_and_add_first_product()
        products_page.click_continue_shopping()
        products_page.hover_and_add_second_product()
        products_page.click_continue_shopping()

        home_page.click_cart_button()
        view_cart_page = ViewCartPage(self.driver)
        assert view_cart_page.is_cart_page_visible()

        view_cart_page.click_checkout_button()
        
        checkout_page = CheckoutPage(self.driver)
        
        assert address1 in checkout_page.get_delivery_address()
        assert address1 in checkout_page.get_billing_address()

        home_page.click_delete_account_button()

        delete_account_page = DeleteAccountPage(self.driver)
        expected_text2 = "ACCOUNT DELETED!"
        assert delete_account_page.get_account_deleted_message() == expected_text2

        delete_account_page.click_contine_button()

        assert home_page.is_app_logo_present()
    
    
    @pytest.mark.regression
    @pytest.mark.checkout      
    def test_24_download_invoice_after_purchase_order(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()

        home_page.click_products_button()
        
        products_page = ProductsPage(self.driver)
        products_page.hover_and_add_first_product()
        products_page.click_continue_shopping()
        products_page.hover_and_add_second_product()
        products_page.click_continue_shopping()

        home_page.click_cart_button()
        view_cart_page = ViewCartPage(self.driver)
        assert view_cart_page.is_cart_page_visible()

        view_cart_page.click_checkout_button()
        view_cart_page.click_register_login_button()

        # filling details in signup page
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_signup_section_present()
        
        name = generate_random_name()
        email = generate_random_email()
        signup_and_login_page.enter_name_in_signup_field(name)
        signup_and_login_page.enter_email_in_signup_field(email)
        signup_and_login_page.click_signup_button()
        
        password = generate_random_password()
        first_name = generate_random_name()
        last_name = generate_random_name()
        company = generate_random_name()
        address1 = generate_random_address()
        address2 = generate_random_address()
        state = generate_random_name()
        city = generate_random_name()
        zipcode = generate_random_phone(6)
        mobile = generate_random_phone()
        
        signup_page = SignupPage(self.driver)
        signup_page.select_title("Mr")
        signup_page.enter_password(password)
        signup_page.select_day(21)
        signup_page.select_month("May")
        signup_page.select_year(2018)
        signup_page.select_newsletter()
        signup_page.select_offers()
        signup_page.enter_first_name(first_name)
        signup_page.enter_last_name(last_name)
        signup_page.enter_company(company)
        signup_page.enter_address1(address1)
        signup_page.enter_address2(address2)
        signup_page.enter_country("India")
        signup_page.enter_state(state)
        signup_page.enter_city(city)
        signup_page.enter_zipcode(zipcode)
        signup_page.enter_mobile(mobile)
        signup_page.click_create_account_button()

        account_created_page = AccountCreatedPage(self.driver)
        assert account_created_page.get_account_created_message() == "ACCOUNT CREATED!"
        
        account_created_page.click_continue_button()

        assert home_page.is_logged_in_as_username_present()
        home_page.click_cart_button()
        view_cart_page.click_checkout_button()
        
        checkout_page = CheckoutPage(self.driver)
        
        assert first_name in checkout_page.get_delivery_name()
        assert address1 in checkout_page.get_delivery_address()
        
        product_names = checkout_page.get_product_names()
        prices = checkout_page.get_product_prices()
        quantities = checkout_page.get_product_quantities()
        totals = checkout_page.get_product_totals()
        
        assert len(product_names) > 0
        assert len(prices) == len(product_names)
        assert len(quantities) == len(product_names)
        assert len(totals) == len(product_names)
                
        message = generate_random_string(12)
        checkout_page.enter_message(message)

        checkout_page.click_place_order_button()

        payment_page = PaymentPage(self.driver)
        assert payment_page.is_payment_page_visible()

        card_holder_name = generate_random_name()
        card_number = generate_random_phone(12)
        cvc = generate_random_phone(3)
        expiration_month = "January"
        expiration_year = 2016
        
        payment_page.enter_name_on_card(card_holder_name)
        payment_page.enter_card_number(card_number)
        payment_page.enter_CVC(cvc)
        payment_page.enter_expiration_month(expiration_month)
        payment_page.enter_expiration_year(expiration_year)
        payment_page.click_confirm_order_button()
        
        payment_done_page = PaymentDonePage(self.driver)
        expected_text1 = "ORDER PLACED!"
        
        assert payment_done_page.get_message() == expected_text1
        
        payment_done_page.click_download_invoice_button()
        
        download_dir = os.path.join(os.getcwd(), "downloads")
        assert is_file_downloaded(download_dir, "invoice"), "Invoice not downloaded"
        
        payment_done_page.click_continue_button()
        home_page.click_delete_account_button()

        delete_account_page = DeleteAccountPage(self.driver)
        expected_text2 = "ACCOUNT DELETED!"
        assert delete_account_page.get_account_deleted_message() == expected_text2

        delete_account_page.click_contine_button()

        assert home_page.is_app_logo_present()