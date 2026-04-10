import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader


@pytest.fixture()
def setup_and_teardown(request):
    config = ConfigReader()
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    
    driver = webdriver.Chrome(chrome_options)
    driver.maximize_window()
    driver.get(config.get_base_url())
    
    request.cls.driver = driver
    yield
    
    driver.quit()