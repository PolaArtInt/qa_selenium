import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

options.page_load_strategy = 'normal'
options.add_argument("--ignore-certificate-errors")
options.add_argument("--disable-cache")

prefs = {
    'download.default_directory': f'{os.getcwd()}/downloads'
}
options.add_experimental_option('prefs', prefs)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)

# Task 1:
# Загрузить любой файл в 'Choose File':
driver.get('https://demoqa.com/upload-download')
upload_field = driver.find_element('xpath', '//input[@type="file"]')
upload_field.send_keys(f'{os.getcwd()}/downloads/mountains.jpg')
time.sleep(3)

# Task 2:
# С помощью цикла for скачать все файлы в папку /downloads:
driver.get('http://the-internet.herokuapp.com/download')

files = driver.find_elements('xpath', '//div[@class="example"]/a')
print(len(files))

for file in files:
    file.click()
time.sleep(3)


