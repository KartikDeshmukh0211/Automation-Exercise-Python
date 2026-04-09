from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ContactUsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    GET_IN_TOUCH_TEXT = (By.XPATH, "//h2[normalize-space()='Get In Touch']")
    NAME_INPUT = (By.XPATH, "//input[@placeholder='Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email']")
    SUBJECT_INPUT = (By.XPATH, "//input[@placeholder='Subject']")
    MESSAGE_INPUT = (By.XPATH, "//textarea[@id='message']")
    UPLOAD_FILE_INPUT = (By.XPATH, "//input[@name='upload_file']")
    SUBMIT_BUTTON = (By.XPATH, "//input[@name='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='status alert alert-success']")
    HOME_BUTTON = (By.XPATH, "//a[@class='btn btn-success']")

    def is_get_in_touch_present(self):
        return self.is_visible(self.GET_IN_TOUCH_TEXT)

    def enter_name(self, name):
        self.send_keys(self.NAME_INPUT, name)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    def enter_subject(self, subject):
        self.send_keys(self.SUBJECT_INPUT, subject)

    def enter_message(self, message):
        self.send_keys(self.MESSAGE_INPUT, message)
        
    def upload_file(self, file_path):
        self.send_keys(self.UPLOAD_FILE_INPUT, file_path)

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)
        
    def click_ok_on_alert(self):
        self.accept_alert()
        
    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def click_home_button(self):
        self.click(self.HOME_BUTTON)

    