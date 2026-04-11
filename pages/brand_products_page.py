from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class BrandProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    BRAND_TITLE = (By.XPATH, "//h2[@class='title text-center']")
    PRODUCTS = (By.XPATH, "//div[@class='product-image-wrapper']")

    def get_brand_title_text(self):
        return self.get_text(self.BRAND_TITLE)

    def is_products_visible(self):
        return len(self.driver.find_elements(*self.PRODUCTS)) > 0