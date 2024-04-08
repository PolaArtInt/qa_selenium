import time
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://umcabango.org/'
title = 'Umcabango Design | Graphic design with smile and magic! :-)'

driver.get(url)  # открытие страницы
src_code = driver.page_source  # получение source code

curr_url = driver.current_url  # определение текущего адреса страницы
curr_title = driver.title  # определение title страницы
assert curr_url == url, 'Wrong url'  # проверка соответствия текущего адреса ожидаемому
assert curr_title == title, 'Wrong title'

print(curr_url)
print(curr_title)
# print(src_code)

# проверка того, что элемент присутствует на странице:
tv_elem = driver.find_element('xpath', '//div[@class="tv_wrap"]')
tv_elem_cl = 'tv_wrap'
assert tv_elem_cl in src_code, 'Element not found'
assert tv_elem_cl in driver.page_source, 'Element not found'
# print(tv_elem)

time.sleep(2)
