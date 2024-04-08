import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    options.add_argument('--window-size=1920,1080')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


def test_make_screenshot(driver, wait):
    driver.get('https://www.google.com')
    driver.save_screenshot('google.png')

