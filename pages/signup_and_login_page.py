from selenium.webdriver.common.by import By

from pages.base_page import BasePage

class SignupAndLoginPage(BasePage):
    def __init__(self, driver):
        # self.driver = driver
        super().__init__(driver)

    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='login-email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    LOGIN_TEXT = (By.XPATH, "//h2[normalize-space()='Login to your account']")
    WARNING_MESSAGE_LOGIN = (By.XPATH, "//p[normalize-space()='Your email or password is incorrect!']")
    SIGNUP_TEXT = (By.XPATH, "//h2[normalize-space()='New User Signup!']")
    SIGNUP_NAME_INPUT = (By.XPATH, "//input[@placeholder='Name']")
    SIGNUP_EMAIL_INPUT = (By.XPATH, "//input[@data-qa='signup-email']")
    SIGNUP_BUTTON = (By.XPATH, "//button[normalize-space()='Signup']")
    WARNING_MESSAGE_SIGNUP = (By.XPATH, "//p[normalize-space()='Email Address already exist!']")
    
    def enter_email_in_login_field(self, email):
        # self.driver.find_element(*self.LOGIN_EMAIL_INPUT).send_keys(email)
        self.send_keys(self.LOGIN_EMAIL_INPUT, email)
        
    def enter_password_in_login_field(self, password):
        # self.driver.find_element(*self.LOGIN_PASSWORD_INPUT).send_keys(password)
        self.send_keys(self.LOGIN_PASSWORD_INPUT, password)
        
    def click_login_button(self):
        # self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.click(self.LOGIN_BUTTON)
        
    def is_login_section_present(self):
        return self.is_visible(self.LOGIN_TEXT)
    
    def is_signup_section_present(self):
        return self.is_visible(self.SIGNUP_TEXT)
    
    def get_warning_message_for_login(self):
        return self.get_text(self.WARNING_MESSAGE_LOGIN)
    
    def get_warning_message_for_signup(self):
        return self.get_text(self.WARNING_MESSAGE_SIGNUP)
    
    def enter_email_in_signup_field(self, email):
        self.send_keys(self.SIGNUP_EMAIL_INPUT, email)
        
    def enter_name_in_signup_field(self, name):
        self.send_keys(self.SIGNUP_NAME_INPUT, name)
        
    def click_signup_button(self):
        self.click(self.SIGNUP_BUTTON)
    