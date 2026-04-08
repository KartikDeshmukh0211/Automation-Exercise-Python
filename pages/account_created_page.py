from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AccountCreatedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//b[normalize-space()='Account Created!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[normalize-space()='Continue']")

    def get_account_created_message(self):
        return self.get_text(self.ACCOUNT_CREATED_TEXT)

    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    