# implicit wait - неявное ожидание
# Указывается 1 раз в коде и работает для всей сессии
# В основном применяется для find_element() и find_elements(),
# потому что эти методы запрашивают обновления элемента на странице
# При проверке на исчезновение элемента будет задерживать тесты
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

options.page_load_strategy = 'normal'
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-cache")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(10)  # неявное ожидание

driver.get('https://demoqa.com/dynamic-properties')
btn_loc = ('xpath', '//button[@id="visibleAfter"]')

visible_after_5_seconds_btn = driver.find_element(*btn_loc)
visible_after_5_seconds_btn.click()
time.sleep(2)
