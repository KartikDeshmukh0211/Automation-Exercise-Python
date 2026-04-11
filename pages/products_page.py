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
    BRANDS_SIDEBAR = (By.XPATH, "//div[@class='brands_products']")
    BRAND_LINKS = (By.XPATH, "//div[@class='brands_products']//a")
    PRODUCT_LIST = (By.XPATH, "//div[@class='features_items']")
    PRODUCT_NAMES = (By.XPATH, "//div[@class='productinfo text-center']/p")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//a[contains(text(),'Add to cart')]")
    
    
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
        
    def is_brands_sidebar_visible(self):
        return self.is_visible(self.BRANDS_SIDEBAR)

    def click_brand(self, brand_name):
        locator = (By.XPATH, f"//div[@class='brands_products']//a[contains(normalize-space(),'{brand_name}')]")
        self.click(locator)
        
    def add_all_products_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS) #for getting  count of buttons

        for i in range(len(buttons)):
            # for avoiding StaleElementReferenceException as DOM updates when we do some actions.....
            buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS) 

            self.driver.execute_script("arguments[0].click();", buttons[i])
            self.click(self.CONTINUE_SHOPPING_BTN)

    def get_searched_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]