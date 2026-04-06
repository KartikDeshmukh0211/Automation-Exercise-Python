import pytest
from selenium import webdriver

from utils.config_reader import ConfigReader


@pytest.fixture()
def setup_and_teardown(request):
    config = ConfigReader()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(config.get_base_url())
    
    request.cls.driver = driver
    yield
    
    driver.quit()