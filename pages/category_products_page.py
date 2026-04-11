from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CategoryProductsPage(BasePage):    
    def __init__(self, driver):
        super().__init__(driver)

    CATEGORY_TITLE = (By.XPATH, "//h2[@class='title text-center']")

    def get_category_title_text(self):
        return self.get_text(self.CATEGORY_TITLE)