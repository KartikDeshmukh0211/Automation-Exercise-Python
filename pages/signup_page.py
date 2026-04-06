from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    ENTER_ACCOUNT_INFO_TEXT = (By.XPATH, "//b[normalize-space()='Enter Account Information']")
    TITLE_LIST = (By.CLASS_NAME, "top")
    PASSWORD_TEXT = (By.XPATH, "//input[@id='password']")
    DAY_DROPDOWN = (By.XPATH, "//select[@id='days']")
    MONTH_DROPDOWN = (By.XPATH, "//select[@id='months']")
    YEAR_DROPDOWN = (By.XPATH, "//select[@id='years']")
    CHECKBOXES = (By.CLASS_NAME, "checker")
    FIRST_NAME_INPUT = (By.XPATH, "//input[@id='first_name']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@id='last_name']")
    COMPANY_INPUT = (By.XPATH, "//input[@id='company']")
    ADDRESS1_INPUT = (By.XPATH, "//input[@id='address1']")
    ADDRESS2_INPUT = (By.XPATH, "//input[@id='address2']")
    STATE_INPUT = (By.XPATH, "//input[@id='state']")
    CITY_INPUT = (By.XPATH, "//input[@id='city']")
    ZIPCODE_INPUT = (By.XPATH, "//input[@id='zipcode']")
    MOBILE_NUMBER_INPUT = (By.XPATH, "//input[@id='mobile_number']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Create Account']")
    COUNTRY_DROPDOWN = (By.XPATH, "//select[@id='country']")

        
    def is_enter_account_info_present(self):
        return self.is_visible(self.ENTER_ACCOUNT_INFO_TEXT)

    # def select_title(self, title):
    #     if title.__eq__("Mr."):
            