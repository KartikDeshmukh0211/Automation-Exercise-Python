import allure
import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.config_reader import ConfigReader

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item.instance, "driver", None)

        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)
            # print(f"Screenshot saved: {file_path}")
            
            # Attaching screnshots to Allure
            with open(file_path, "rb") as image:
                allure.attach(
                    image.read(),
                    name=file_name,
                    attachment_type=allure.attachment_type.PNG
                )
        
@pytest.fixture()
def setup_and_teardown(request):
    config = ConfigReader()
    
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)
    
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    
    driver = webdriver.Chrome(options=chrome_options)   
    driver.maximize_window()
    driver.get(config.get_base_url())
    
    request.cls.driver = driver
    yield
    
    driver.quit()