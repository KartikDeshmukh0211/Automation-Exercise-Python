from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ViewCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    PRODUCT_NAMES = (By.CLASS_NAME, "cart_description")
    PRODUCT_PRICES = (By.CLASS_NAME, "cart_price")
    PRODUCT_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    PRODUCT_TOTAL = (By.CLASS_NAME, "cart_total")
    PRODUCT_QUANTITY = (By.XPATH, "//td[@class='cart_quantity']")
    CART_PAGE_INFO = (By.XPATH, "//li[@class='active']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Proceed To Checkout']")
    REGISTER_LOGIN_BUTTON = (By.XPATH, "//u[normalize-space()='Register / Login']")
    
    def is_cart_page_visible(self):
        return self.is_visible(self.CART_PAGE_INFO)
    
    def get_products_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_NAMES))

    def get_prices(self):
        return [p.text for p in self.driver.find_elements(*self.PRODUCT_PRICES)]

    def get_quantities(self):
        return [q.text for q in self.driver.find_elements(*self.PRODUCT_QUANTITY)]

    def get_totals(self):
        return [t.text for t in self.driver.find_elements(*self.PRODUCT_TOTAL)]

    def get_product_quantity(self):
        text = self.get_text(self.PRODUCT_QUANTITY)
        return int(text)
    
    def click_checkout_button(self):
        self.click(self.CHECKOUT_BUTTON)
        
    def click_register_login_button(self):
        self.click(self.REGISTER_LOGIN_BUTTON)