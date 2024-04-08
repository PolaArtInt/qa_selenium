import time
from selenium import webdriver

driver = webdriver.Chrome()

url_1 = 'https://umcabango.org/'
url_2 = 'https://www.google.com/'

# go to umcabango:
driver.get(url_1)
curr_title = driver.title
print(f'Current page title: {curr_title}')
time.sleep(2)

# go to google:
driver.get(url_2)
curr_title = driver.title
print(f'Current page title: {curr_title}')
time.sleep(2)

# go back to umcabango:
driver.back()
curr_url = driver.current_url
assert curr_url == url_1, f'Current url is wrong: {curr_url}'
time.sleep(2)

# stay on umcabango:
driver.refresh()
curr_url = driver.current_url
print(f'Current page url: {curr_url}')
time.sleep(2)

# go forward to google:
driver.forward()
curr_url = driver.current_url
assert curr_url == url_2, f'Current url is wrong: {curr_url}'
time.sleep(2)

print('Process finished with exit code 0. You\'re awesome, Pola!')



