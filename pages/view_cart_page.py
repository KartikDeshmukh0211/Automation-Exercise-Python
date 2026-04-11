from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ViewCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    # PRODUCT_NAMES = (By.CLASS_NAME, "cart_description")
    PRODUCT_PRICES = (By.CLASS_NAME, "cart_price")
    # PRODUCT_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    PRODUCT_TOTAL = (By.CLASS_NAME, "cart_total")
    PRODUCT_NAMES = (By.XPATH, "//td[@class='cart_description']//a")
    PRODUCT_QUANTITY = (By.XPATH, "//td[@class='cart_quantity']//button")
    CART_PAGE_INFO = (By.XPATH, "//li[@class='active']")
    CHECKOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Proceed To Checkout']")
    REGISTER_LOGIN_BUTTON = (By.XPATH, "//u[normalize-space()='Register / Login']")
    PRODUCT_REMOVE_BUTTON = (By.XPATH, "//a[@class='cart_quantity_delete']")
    CART_EMPTY_TEXT = (By.XPATH, "//b[normalize-space()='Cart is empty!']")
    
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
        
    def clilck_remove_product_button(self):
        self.click(self.PRODUCT_REMOVE_BUTTON)
        
    def is_cart_empty(self):
        return self.is_visible(self.CART_EMPTY_TEXT)
    
    def get_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]