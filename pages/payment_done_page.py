from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class PaymentDonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    ORDER_PLACED_TEXT = (By.XPATH, "//b[normalize-space()='Order Placed!']")
    CONTINUE_BUTTON = (By.XPATH, "//a[normalize-space()='Continue']")
    DOWNLOAD_INVOICE_BUTTON = (By.XPATH, "//a[normalize-space()='Download Invoice']")
    
    def get_message(self):
        return self.get_text(self.ORDER_PLACED_TEXT)
    
    def click_continue_button(self):
        self.click(self.CONTINUE_BUTTON)

    def click_download_invoice_button(self):
        self.click(self.DOWNLOAD_INVOICE_BUTTON)