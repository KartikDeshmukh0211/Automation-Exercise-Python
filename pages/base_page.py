from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # for clicking the element
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        
    # for entering the text
    def send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
        
    # for geting the text
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    # checking if element is visible
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False
    
    # Waiting for the element
    def wait_for_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def check_checkbox(self, locator):
        element = self.wait_for_element(locator)
        if not element.is_selected():
            element.click()