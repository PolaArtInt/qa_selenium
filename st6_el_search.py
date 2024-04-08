import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = 'https://www.w3schools.com/'

driver.get(url)
time.sleep(2)

nav_links = driver.find_elements(By.CSS_SELECTOR, '#subtopnav>a')
# print(len(nav_links))  # 41 links in menu
time.sleep(2)

for el in nav_links:
    print(el.text)

python_link = nav_links[4]
python_link.click()
time.sleep(2)

python_h1 = driver.find_element('tag name', 'h1')
assert python_h1.text == 'Python Tutorial'
print(python_h1.text)
