from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DeleteAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//b[normalize-space()='Account Deleted!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[normalize-space()='Continue']")
    
    def get_account_deleted_message(self):
        return self.get_text(self.ACCOUNT_DELETED_TEXT)
    
    def click_contine_button(self):
        self.click(self.CONTINUE_BUTTON)