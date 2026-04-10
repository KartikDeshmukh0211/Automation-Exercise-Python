from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductDetailsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    PRODUCT_DETAILS = (By.XPATH, "//div[@class='product-information']")
    PRODUCT_NAME_TEXT = (By.XPATH, "//h2[normalize-space()='Blue Top']")
    CATEGORY_TEXT = (By.XPATH, "//p[normalize-space()='Category: Women > Tops']")
    PRICE_TEXT = (By.XPATH, "//span[normalize-space()='Rs. 500']")
    AVAILABILITY_TEXT = (By.XPATH, "//b[normalize-space()='Availability:']")
    CONDITION_TEXT = (By.XPATH, "//b[normalize-space()='Condition:']")
    BRAND_TEXT = (By.XPATH, "//b[normalize-space()='Brand:']")
    QUANTITY_INPUT = (By.XPATH, "//input[@id='quantity']")
    ADD_TO_CART_BTN = (By.XPATH, "//button[normalize-space()='Add to cart']")
    VIEW_CART_BTN = (By.XPATH, "//u[text()='View Cart']")
    
    def is_product_detail_visible(self):
        return self.is_visible(self.PRODUCT_DETAILS)
    
    def is_product_name_present(self):
        return self.is_visible(self.PRODUCT_NAME_TEXT)

    def is_category_visible(self):
        return self.is_visible(self.CATEGORY_TEXT)

    def is_price_visible(self):
        return self.is_visible(self.PRICE_TEXT)

    def is_availability_visible(self):
        return self.is_visible(self.AVAILABILITY_TEXT)

    def is_conditon_visible(self):
        return self.is_visible(self.CONDITION_TEXT)

    def is_brand_visible(self):
        return self.is_visible(self.BRAND_TEXT)
    
    def enter_quantity(self, qty):
        self.send_keys(self.QUANTITY_INPUT, str(qty))

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def click_view_cart(self):
        self.click(self.VIEW_CART_BTN)