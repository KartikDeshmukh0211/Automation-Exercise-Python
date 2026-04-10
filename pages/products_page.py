from itertools import product

from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    ALL_PRODUCTS_TITLE = (By.XPATH, "//h2[normalize-space()='All Products']")
    SEARCH_PRODUCT_INPUT = (By.XPATH, "//input[@id='search_product']")
    SEARCH_BUTTON = (By.XPATH, "//button[@id='submit_search']")
    SEARCHED_PRODUCT_TEXT = (By.XPATH, "//h2[normalize-space()='Searched Products']")
    FIRST_PRODCUT_VIEW_BUTTON = (By.XPATH, "(//a[contains(text(),'View Product')])[1]")
    FIRST_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
    SECOND_PRODUCT = (By.XPATH, "(//div[@class='product-image-wrapper'])[2]")
    FIRST_ADD_TO_CART = (By.XPATH, "(//div[@class='product-overlay']//a[contains(text(),'Add to cart')])[1]")
    SECOND_ADD_TO_CART = (By.XPATH, "(//div[@class='product-overlay']//a[contains(text(),'Add to cart')])[2]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[text()='Continue Shopping']")
    VIEW_CART_BTN = (By.XPATH, "//u[text()='View Cart']")
    
    
    def is_all_products_page_visible(self):
        return self.is_visible(self.ALL_PRODUCTS_TITLE)
        
    def is_product_list_present(self):
        return self.is_visible(self.FIRST_PRODUCT)
    
    def click_first_product_view_button(self):
        self.click(self.FIRST_PRODCUT_VIEW_BUTTON)
        
    def enter_product_in_search_field(self, product_name):
        self.send_keys(self.SEARCH_PRODUCT_INPUT, product_name)
        
    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)

    def is_search_product_text_present(self):
        return self.is_visible(self.SEARCHED_PRODUCT_TEXT)

    def hover_and_add_first_product(self):
        actions = ActionChains(self.driver)
        product = self.wait_for_element(self.FIRST_PRODUCT)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)
        
        actions.move_to_element(product).perform()
        self.click(self.FIRST_ADD_TO_CART)

    def hover_and_add_second_product(self):
        actions = ActionChains(self.driver)
        product = self.wait_for_element(self.SECOND_PRODUCT)
        
        self.driver.execute_script("arguments[0].scrollIntoView(true);", product)

        actions.move_to_element(product).perform()
        self.click(self.SECOND_ADD_TO_CART)

    def click_continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BTN)

    def click_view_cart(self):
        self.click(self.VIEW_CART_BTN)
        
    

