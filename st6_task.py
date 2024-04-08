import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://testautomationpractice.blogspot.com/'

driver.get(url)
time.sleep(2)

wiki_icon = driver.find_element(By.CLASS_NAME, 'wikipedia-icon')
wiki_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
search_btn = driver.find_element(By.CLASS_NAME, 'wikipedia-search-button')
h1 = driver.find_element(By.TAG_NAME, 'h1')

print(wiki_icon.get_dom_attribute('class'))
print(wiki_input.get_dom_attribute('id'))
print(search_btn.get_dom_attribute('type'))
print(h1.text)

time.sleep(2)

