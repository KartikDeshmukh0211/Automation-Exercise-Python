from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    ADDRESS_NAME = (By.XPATH, "//ul[@id='address_delivery']//li[@class='address_firstname address_lastname']")
    ADDRESS_FULL = (By.XPATH, "//ul[@id='address_delivery']//li[@class='address_address1 address_address2'][2]")
    PRODUCT_NAMES = (By.XPATH, "//td[@class='cart_description']/h4/a")
    PRODUCT_PRICES = (By.XPATH, "//td[@class='cart_price']/p")
    PRODUCT_QUANTITY = (By.XPATH, "//td[@class='cart_quantity']/button")
    PRODUCT_TOTAL = (By.XPATH, "//td[@class='cart_total']/p")
    DESCRIPTION_BOX = (By.XPATH, "//textarea[@name='message']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//a[normalize-space()='Place Order']")

    def get_delivery_name(self):
        return self.get_text(self.ADDRESS_NAME)

    def get_delivery_address(self):
        return self.get_text(self.ADDRESS_FULL)

    def get_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def get_product_prices(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_PRICES)]

    def get_product_quantities(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_QUANTITY)]

    def get_product_totals(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_TOTAL)]

    def enter_message(self, message):
        self.send_keys(self.DESCRIPTION_BOX, message)
        
    def click_place_order_button(self):
        self.click(self.PLACE_ORDER_BUTTON)