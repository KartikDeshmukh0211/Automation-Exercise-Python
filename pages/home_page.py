from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class HomePage(BasePage):
    # Constructor
    # even if we dont write the constructor, it will work properly as python will call the default constructor....
    # def __init__(self, driver):
    #     self.driver = driver
        
    # Locators (They are fixed locator, not a variable so keep them constant)
    SIGNUP_AND_LOGIN_BUTTON = (By.XPATH, "//a[normalize-space()='Signup / Login']")
    LOGOUT_BUTTON = (By.XPATH, "//a[normalize-space()='Logout']")
    APP_LOGO = (By.XPATH, "//img[@alt='Website for automation practice']")
    LOGGED_IN_AS_USERNAME = (By.XPATH, "//li[10]//a[1]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//a[normalize-space()='Delete Account']")
    CONTACT_US_BUTTON = (By.XPATH, "//a[normalize-space()='Contact us']")
    TEST_CASES_BUTTON = (By.XPATH, "//a[contains(text(),'Test Cases')]")
    PRODUCTS_BUTTON = (By.XPATH, "//a[@href='/products']")
    CART_BUTTON = (By.XPATH, "//a[normalize-space()='Cart']")
    FOOTER = (By.XPATH, "//footer[@id='footer']")
    SUBSCRIPTION_TEXT = (By.XPATH, "//h2[normalize-space()='Subscription']")
    EMAIL_INPUT = (By.XPATH, "//input[@id='susbscribe_email']")
    ARROW_BUTTON = (By.XPATH, "//button[@id='subscribe']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='alert-success alert']")
    THIRD_VIEW_PRODUCT = (By.XPATH, "(//a[contains(text(),'View Product')])[3]")

    
    # Methods
    def click_sigup_and_login_button(self):
        # * unpacking operator....we need this so that find_element works properly
        # self.driver.find_element(*self.SIGNUP_AND_LOGIN_BUTTON).click()
        self.click(self.SIGNUP_AND_LOGIN_BUTTON)
        
    def is_logout_button_present(self):
        # return self.driver.find_element(*self.LOGOUT_BUTTON).is_displayed()
        return self.is_visible(self.LOGOUT_BUTTON)
    
    def is_app_logo_present(self):
        return self.is_visible(self.APP_LOGO)
    
    def is_logged_in_as_username_present(self):
        return self.is_visible(self.LOGGED_IN_AS_USERNAME)
    
    def click_logout_button(self):
        self.click(self.LOGOUT_BUTTON)
    
    def click_delete_account_button(self):
        self.click(self.DELETE_ACCOUNT_BUTTON)

    def click_contact_us_button(self):
        self.click(self.CONTACT_US_BUTTON)

    def click_test_cases_button(self):
        self.click(self.TEST_CASES_BUTTON)
        
    def click_products_button(self):
        self.click(self.PRODUCTS_BUTTON)
    
    def click_cart_button(self):
        self.click(self.CART_BUTTON)
        
    def scrool_to_footer(self):
        # element = self.wait_for_element(self.FOOTER)
        # self.driver.execute_script("arguments[0].scroolIntoView(true)", element)
        
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def is_subscription_text_visible(self):
        return self.is_visible(self.SUBSCRIPTION_TEXT)

    def enter_subscription_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def click_arrow_button(self):
        self.click(self.ARROW_BUTTON)

    def get_subscription_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
    
    def click_third_view_product(self):
        self.click(self.THIRD_VIEW_PRODUCT)