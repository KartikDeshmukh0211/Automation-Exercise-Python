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

    