from pages.home_page import HomePage
from pages.signup_and_login_page import SignupAndLoginPage
from tests.base_test import BaseTest


class TestLogin(BaseTest):
    def test_02_login_with_correct_email_and_password(self):

        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        
        login_page = SignupAndLoginPage(self.driver)
        assert login_page.is_login_section_present()
        
        login_page.enter_email_in_login_field("kartikdeshmukh58@gmail.com")
        login_page.enter_password_in_login_field("123456")
        login_page.click_login_button()
        
        assert home_page.is_logged_in_as_username_present()
        
        # we will avoid deleting the account during login steps inorder to preserve account
        
    def test_03_login_with_incorrect_email_and_password(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_sigup_and_login_button()
        
        login_page = SignupAndLoginPage(self.driver)
        assert login_page.is_login_section_present()
        
        expected_text = "Your email or password is incorrect!"
        
        # valid email and invalid password
        login_page.enter_email_in_login_field("kartikdeshmukh58@gmail.com")
        login_page.enter_password_in_login_field("12345")
        login_page.click_login_button()
        assert login_page.get_warning_message().__eq__(expected_text)
        
        # invalid email and valid password
        login_page.enter_email_in_login_field("kaeadfadf73shmukh58@gmail.com")
        login_page.enter_password_in_login_field("123456")
        login_page.click_login_button()
        
        assert login_page.get_warning_message().__eq__(expected_text)