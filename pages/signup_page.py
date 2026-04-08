from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SignupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    ENTER_ACCOUNT_INFO_TEXT = (By.XPATH, "//b[normalize-space()='Enter Account Information']")
    MR_RADIO = (By.ID, "id_gender1")
    MRS_RADIO = (By.ID, "id_gender2")
    PASSWORD_TEXT = (By.XPATH, "//input[@id='password']")
    DAY_DROPDOWN = (By.XPATH, "//select[@id='days']")
    MONTH_DROPDOWN = (By.XPATH, "//select[@id='months']")
    YEAR_DROPDOWN = (By.XPATH, "//select[@id='years']")
    NEWS_LETTER_CHECKBOX = (By.ID, "newsletter")
    OPTIN_CHECKBOX = (By.ID, "optin")
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

    def select_title(self, title):
        if title == "Mr":
            self.click(self.MR_RADIO)
        else :
            self.click(self.MRS_RADIO)
            
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_TEXT, password)
        
    # functions accessing dropdowns
    def select_day(self, day):
        web_element = self.wait_for_element(self.DAY_DROPDOWN)
        dropdown = Select(web_element)
        dropdown.select_by_visible_text(str(day))
        
    def select_month(self, month):
        dropdown = Select(self.wait_for_element(self.MONTH_DROPDOWN))
        dropdown.select_by_visible_text(month)
        
    def select_year(self, year):
        dropdown = Select(self.wait_for_element(self.YEAR_DROPDOWN))
        dropdown.select_by_visible_text(str(year))
        
    def select_newsletter(self):
        self.check_checkbox(self.NEWS_LETTER_CHECKBOX)

    def select_offers(self):
        self.check_checkbox(self.OPTIN_CHECKBOX)
        
    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME_INPUT, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME_INPUT, last_name)

    def enter_company(self, company):
        self.send_keys(self.COMPANY_INPUT, company)

    def enter_address1(self, address):
        self.send_keys(self.ADDRESS1_INPUT, address)

    def enter_address2(self, address):
        self.send_keys(self.ADDRESS2_INPUT, address)
        
    def enter_country(self, country):
        dropdown = Select(self.wait_for_element(self.COUNTRY_DROPDOWN))
        dropdown.select_by_visible_text(country)

    def enter_state(self, state):
        self.send_keys(self.STATE_INPUT, state)

    def enter_city(self, city):
        self.send_keys(self.CITY_INPUT, city)

    def enter_zipcode(self, zipcode):
        self.send_keys(self.ZIPCODE_INPUT, zipcode)

    def enter_mobile(self, mobile):
        self.send_keys(self.MOBILE_NUMBER_INPUT, mobile)
        
    def click_create_account_button(self):
        self.click(self.CREATE_ACCOUNT_BUTTON)