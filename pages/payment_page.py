from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PaymentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    PAYEMENT_PAGE = (By.XPATH, "//li[@class='active']")
    NAME_ON_CARD_INPUT = (By.XPATH, "//input[@name='name_on_card']")
    CARD_NUMBER_INPUT = (By.XPATH, "//input[@name='card_number']")
    CVC_INPUT = (By.XPATH, "//input[@placeholder='ex. 311']")
    EXPIRATION_MONTH_INPUT = (By.XPATH, "//input[@placeholder='MM']")
    EXPIRATION_YEAR_INPUT = (By.XPATH, "//input[@placeholder='YYYY']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[@id='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(),'Your order has been placed successfully!')]")

    def is_payment_page_visible(self):
        return self.is_visible(self.PAYEMENT_PAGE)
        
    def enter_name_on_card(self, name):
        self.send_keys(self.NAME_ON_CARD_INPUT, str(name))

    def enter_card_number(self, number):
        self.send_keys(self.CARD_NUMBER_INPUT, str(number))

    def enter_CVC(self, cvc):
        self.send_keys(self.CVC_INPUT, str(cvc))

    def enter_expiration_month(self, month):
        self.send_keys(self.EXPIRATION_MONTH_INPUT, month)

    def enter_expiration_year(self, year):
        self.send_keys(self.EXPIRATION_YEAR_INPUT, str(year))

    def click_confirm_order_button(self):
        self.click(self.CONFIRM_ORDER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)