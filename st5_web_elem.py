import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# By uses:
# find_element(By.ID, 'id')
# find_element(By.NAME, 'name')
# find_element(By.XPATH, 'xpath')
# find_element(By.LINK_TEXT, 'link text')
# find_element(By.PARTIAL_LINK_TEXT, 'partial link text')
# find_element(By.TAG_NAME, 'tag name')
# find_element(By.CLASS_NAME, 'class name')
# find_element(By.CSS_SELECTOR, 'css selector')

driver = webdriver.Chrome()

url = 'https://umcabango.org/'

driver.get(url)
time.sleep(2)

# print(driver.find_element('xpath', '//a[@href="#openHidden"]'))  # without By
# print(driver.find_element(By.CSS_SELECTOR, '.on-off'))

dev_link = driver.find_element(By.CSS_SELECTOR, '.dev_link>a')
nav = driver.find_element(By.CSS_SELECTOR, '#site-navigation')
hidden_nav = driver.find_element(By.CSS_SELECTOR, '.hidden-bars')

dev_link.click()  # клик по элементу
time.sleep(3)

# find dom attributes:
# print(dev_link.get_dom_attribute('href'))  # https://www.linkedin.com/in/pola-g/

# print(nav.get_dom_attribute('class'))  # nav
# print(nav.get_dom_attribute('id'))  # site-navigation
# print(nav.get_dom_attribute('name'))  # None

# print(hidden_nav.get_dom_attribute('href'))  # #openHidden


