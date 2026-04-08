from pages.account_created_page import AccountCreatedPage
from pages.delete_account_page import DeleteAccountPage
from pages.home_page import HomePage
from pages.signup_and_login_page import SignupAndLoginPage
from pages.signup_page import SignupPage
from tests.base_test import BaseTest
from utils.config_reader import ConfigReader
from utils.data_generator import *


class TestAuthentication(BaseTest):
    def test_01_register_user(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
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
        home_page.click_delete_account_button()
        
        delete_account_page = DeleteAccountPage(self.driver)
        assert delete_account_page.get_account_deleted_message() == "ACCOUNT DELETED!"
        delete_account_page.click_contine_button()
        
        assert home_page.is_app_logo_present()           
            
    def test_02_login_with_correct_email_and_password(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_login_section_present()
        
        config = ConfigReader()
        signup_and_login_page.enter_email_in_login_field(config.get_email())
        signup_and_login_page.enter_password_in_login_field(config.get_password())
        signup_and_login_page.click_login_button()
        
        assert home_page.is_logged_in_as_username_present()
        
        # we will avoid deleting the account during login steps inorder to preserve account
        
    def test_03_login_with_incorrect_email_and_password(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_login_section_present()
        
        expected_text = "Your email or password is incorrect!"
        config = ConfigReader()
        # valid email and invalid password
        signup_and_login_page.enter_email_in_login_field(config.get_email())
        signup_and_login_page.enter_password_in_login_field("wrongpass")
        signup_and_login_page.click_login_button()
        assert signup_and_login_page.get_warning_message_for_login().__eq__(expected_text)
        
        # invalid email and valid password
        signup_and_login_page.enter_email_in_login_field("wrongmail@gmail.com")
        signup_and_login_page.enter_password_in_login_field(config.get_password())
        signup_and_login_page.click_login_button()
        
        assert signup_and_login_page.get_warning_message_for_login().__eq__(expected_text)
        
    def test_04_logout_user(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_login_section_present()
        
        config = ConfigReader()
        signup_and_login_page.enter_email_in_login_field(config.get_email())
        signup_and_login_page.enter_password_in_login_field(config.get_password())
        signup_and_login_page.click_login_button()
        
        home_page.click_logout_button()
        assert signup_and_login_page.is_login_section_present()
        
    def test_05_register_user_with_existing_email(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        signup_and_login_page = SignupAndLoginPage(self.driver)
        assert signup_and_login_page.is_signup_section_present()

        config = ConfigReader()
        name = generate_random_name()
        email = config.get_email() # this is already registered email
        
        signup_and_login_page.enter_name_in_signup_field(name)
        signup_and_login_page.enter_email_in_signup_field(email)
        signup_and_login_page.click_signup_button()

        expected_text = "Email Address already exist!"
        assert signup_and_login_page.get_warning_message_for_signup() == expected_text
        