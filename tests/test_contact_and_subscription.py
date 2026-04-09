import os

from pages.contact_us_page import ContactUsPage
from pages.home_page import HomePage
from tests.base_test import BaseTest
from utils.data_generator import *


class TestContactAndSubscription(BaseTest):
    def test_06_contact_us_form(self):
        home_page = HomePage(self.driver)
        assert home_page.is_app_logo_present()
        
        home_page.click_contact_us_button()
        contact_us_page = ContactUsPage(self.driver)

        assert contact_us_page.is_get_in_touch_present()

        name = generate_random_name()
        email = generate_random_email()
        subject = generate_random_string(12)
        message = generate_random_string(9) + " " + generate_random_string(9) + " " +  generate_random_string(9)
        file_path = os.path.join(os.getcwd(), "test_data", "sample.txt")

        contact_us_page.enter_name(name)
        contact_us_page.enter_email(email)
        contact_us_page.enter_subject(subject)
        contact_us_page.enter_message(message)
        contact_us_page.upload_file(file_path)
        contact_us_page.click_submit_button()
        contact_us_page.click_ok_on_alert()
        
        expected_message = "Success! Your details have been submitted successfully."
        assert contact_us_page.get_success_message() == expected_message

        contact_us_page.click_home_button()
        assert home_page.is_app_logo_present()
        