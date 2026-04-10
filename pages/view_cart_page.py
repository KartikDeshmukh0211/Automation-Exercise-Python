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