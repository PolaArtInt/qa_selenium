import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://umcabango.org/about/')  # открытие страницы
time.sleep(2)
driver.get('https://umcabango.org/')  # открытие другой страницы
time.sleep(2)
driver.back()  # назад
time.sleep(2)
driver.forward()  # вперёд
time.sleep(2)
driver.refresh()  # перезагрузить
time.sleep(2)

