import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://umcabango.org/'

driver.get(url)
time.sleep(2)

btn_on_off = driver.find_element(By.CLASS_NAME, 'on-off')
btn_on_off.click()
time.sleep(3)

picture = driver.find_element(By.CSS_SELECTOR, '.tv_wrap>a>img')
assert picture.get_dom_attribute('class') == 'off', 'TV has to be off'

btn_on_off.click()
time.sleep(2)
assert picture.get_dom_attribute('class') == '', 'TV has to be on'

# btn = driver.find_element(By.CSS_SELECTOR, '#menu-item-34 a')
# btn.click()
