import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    options.add_argument('--window-size=1920,1080')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/123.0.0.0 Safari/537.36")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def wait(driver):
    # создание объекта wait:
    wait = WebDriverWait(driver, timeout=15)
    return wait


url = 'https://demoqa.com/alerts'


def test_alert_accept(driver, wait):
    driver.get(url)

    alert_call_btn = ('xpath', '//button[@id="alertButton"]')
    wait.until(ec.visibility_of_element_located(alert_call_btn)).click()
    alert = wait.until(ec.alert_is_present())
    driver.switch_to.alert.accept()


def test_alert_dismiss(driver, wait):
    driver.get(url)

    alert_call_btn = ('xpath', '//button[@id="confirmButton"]')
    wait.until(ec.visibility_of_element_located(alert_call_btn)).click()
    alert = wait.until(ec.alert_is_present())
    time.sleep(3)
    driver.switch_to.alert.dismiss()
    text = driver.find_element('xpath', '//span[@id="confirmResult"]').text
    print(text)


def test_alert_get_text(driver, wait):
    driver.get(url)

    alert_call_btn = ('xpath', '//button[@id="alertButton"]')
    wait.until(ec.visibility_of_element_located(alert_call_btn)).click()
    time.sleep(3)
    alert = wait.until(ec.alert_is_present())
    time.sleep(3)
    alert_text = driver.switch_to.alert.text
    print(alert_text)


def test_send_text_to_alert(driver, wait):
    driver.get(url)

    alert_call_btn = ('xpath', '//button[@id="promtButton"]')
    wait.until(ec.visibility_of_element_located(alert_call_btn)).click()
    alert = wait.until(ec.alert_is_present())
    time.sleep(3)
    alert_text = driver.switch_to.alert
    alert_text.send_keys('Hello')
    time.sleep(3)
    alert.accept()
    time.sleep(3)

