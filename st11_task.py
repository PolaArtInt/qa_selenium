import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# импорты для явного ожидания:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
    # создание объекта wait:
    wait = WebDriverWait(driver, timeout=15)
    return wait


url = 'https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver'


# 1.Кликнуть на кнопку “Change Text to Selenium Webdriver” и дождаться изменения текста элемента рядом:
def test_change_text_btn(driver, wait):
    driver.get(url)

    change_text_btn = ('xpath', '//button[@id="populate-text"]')
    next_elem = ('xpath', '//h2[@id="h2"]')
    text_before = driver.find_element(*next_elem).text
    assert text_before == 'site', 'wrong text'

    wait.until(ec.visibility_of_element_located(change_text_btn)).click()
    wait.until(ec.text_to_be_present_in_element(next_elem, 'Selenium Webdriver'))

    text_after = driver.find_element(*next_elem).text
    assert text_after == 'Selenium Webdriver', 'wrong text'


# 2.Кликнуть на кнопку “Display button after 10 seconds” и дождаться появления кнопки “Enabled”:
def test_display_btn_after(driver, wait):
    driver.get(url)

    display_btn = ('xpath', '//button[@id="display-other-button"]')
    enabled_btn = ('xpath', '//button[@id="hidden"]')

    wait.until(ec.visibility_of_element_located(display_btn)).click()
    btn_visible = wait.until(ec.visibility_of_element_located(enabled_btn))

    assert btn_visible, 'Button not appearing'


# 3.Кликнуть на кнопку “Enable button after 10 seconds" и дождаться кликабельности кнопки “Button”:
def test_enable_btn(driver, wait):
    driver.get(url)

    enable_btn = ('xpath', '//button[@id="enable-button"]')
    next_btn = ('xpath', '//button[@id="disable"]')

    wait.until(ec.visibility_of_element_located(enable_btn)).click()
    btn_enabled = wait.until(ec.element_to_be_clickable(next_btn))

    assert btn_enabled, 'Button disabled'


# 4.Кликнуть на кнопку “Click me, to Open an alert after 5 seconds” и дождаться открытия алерта:
def test_click_me_btn(driver, wait):
    driver.get(url)

    click_me_btn = ('xpath', '//button[@id="alert"]')

    wait.until(ec.visibility_of_element_located(click_me_btn)).click()
    is_alert = wait.until(ec.alert_is_present())

    assert is_alert, 'Alert not present'
