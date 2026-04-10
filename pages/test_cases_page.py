from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TestCasesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    TEST_CASES_MESSAGE = (By.XPATH, "//b[normalize-space()='Test Cases']")
    
    def get_test_cases_text(self):
        return self.get_text(self.TEST_CASES_MESSAGE)