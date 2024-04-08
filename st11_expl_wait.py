# explicit wait - явное ожидание
# ожидание конкретного условия, появления элемента, исчезновения элемента, изменения текста и т.д.
# Обьявляется только там где нужно
# Ожидает выполнения нужного условия
# Проверка на отсутствие элемента, может быть условием к завершению теста, так как можно проверить,
# что элемент пропал и сразу завершить тест, а не ждать

# wait.until(EC.condition(locator), message="Ваше кастомное сообщение при ошибке"):
#     wait.until(EC.visibility_of_element(('xpath', '//button[@id="login_button"]')),
#                                                   message="Кнопка 'Войти' не найдена")

import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# импорты для явного ожидания:
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()

options.page_load_strategy = 'normal'
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-cache")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)


@pytest.fixture()
def wait():
    # создание объекта wait:
    wait = WebDriverWait(driver, timeout=15, poll_frequency=1)
    return wait


def test_visibility(wait):
    driver.get('https://demoqa.com/dynamic-properties')

    visible_after_5_seconds_btn = ('xpath', '//button[@id="visibleAfter"]')
    enable_in_5_seconds_btn = ('xpath', '//button[@id="enableAfter"]')

    wait.until(ec.visibility_of_element_located(visible_after_5_seconds_btn)).click()
    time.sleep(2)
    wait.until(ec.element_to_be_clickable(enable_in_5_seconds_btn)).click()
    time.sleep(2)
    driver.quit()


def test_removed_btn(wait):
    driver.get('http://the-internet.herokuapp.com/dynamic_controls')

    removed_btn = ('xpath', '//button[text()="Remove"]')

    driver.find_element(*removed_btn).click()
    wait.until(ec.invisibility_of_element_located(removed_btn))
    time.sleep(2)
    print('Button successfully removed')

    driver.quit()


def test_clickable_input(wait):
    driver.get('http://the-internet.herokuapp.com/dynamic_controls')

    enable_btn = ('xpath', '//button[text()="Enable"]')
    text_field = ('xpath', '//form[@id="input-example"]/input')

    wait.until(ec.element_to_be_clickable(enable_btn)).click()
    field_is_clickable = wait.until(ec.element_to_be_clickable(text_field))
    field_is_clickable.send_keys('Hello')
    time.sleep(2)

    assert field_is_clickable.get_attribute('value'), 'No value in text field'
    time.sleep(2)
    print('Input is clickable', field_is_clickable.get_attribute('value'))

    final_text = wait.until(ec.text_to_be_present_in_element_value(text_field, 'Hello'))
    assert final_text, 'Value of text field is present in element value'
    time.sleep(2)

    driver.quit()


# expected_conditions - (ожидают, что):
# wait.until(ec.title_is('expected page title')) - заголовок стр. будет точно соотв. тексту
# wait.until(ec.title_contains('expected text')) - заголовок стр. будет содержать заданный текст
# wait.until(ec.url_to_be('https://...')) - ожидаемый url
# wait.until(ec.url_contains('expected')) - url содерж. ожидаемый текст
# wait.until(ec.presence_of_element_located('xpath', '')) - элемент будет присутствовать в DOM
# wait.until(ec.visibility_of_element_located('xpath', '')) - элемент станет видимым
# wait.until(ec.visibility_of(driver.find_element('xpath', ''))) - элемент станет видимым и отображаемым на стр.
# wait.until(ec.invisibility_of_element_located('xpath', '')) - элемент станет невидимым
# wait.until(ec.text_to_be_present_in_element(('xpath', ''), 'text expected')) - появления текста в элементе
# wait.until(ec.text_to_be_present_in_element_value(('xpath', ''), 'text expected')) - появления текста в значении элем.
# wait.until(ec.element_to_be_clickable('xpath', '')) - элемент станет кликабельным
# wait.until(ec.element_to_be_selected('xpath', '')) - элемент будет выбран
# wait.until(ec.element_selection_state_to_be(('xpath', ''), True)) - состояние выбора будет соотв. true/false
# wait.until(ec.element_located_selection_state_to_be(('xpath', ''), True))) - сост. выбора по лок-ру будет соотв. t/f
# wait.until(ec.frame_to_be_available_and_switch_to_it('xpath', '')) - фрейм будет доступен и переключиться на него
# wait.until(ec.alert_is_present()) - что появится алерт

