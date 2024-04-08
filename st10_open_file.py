import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()

options.page_load_strategy = 'normal'

# options.add_argument("--headless")
# options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
# options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-cache")

# download:
# prefs - специфические настройки браузера:
prefs = {
    'download.default_directory': f'{os.getcwd()}/downloads',  # дефолтная директория для загрузок
    'safebrowsing.enabled': False
}
# добавить эту настройку в опции:
options.add_experimental_option('prefs', prefs)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)

# download:
# driver.get('http://the-internet.herokuapp.com/download')
#
# elems = driver.find_elements('xpath', '//a')
# elems[8].click()


# upload:
# driver.get('https://demoqa.com/upload-download')
#
# upload_field = driver.find_element('xpath', '//input[@type="file"]')
# upload_field.send_keys(f'{os.getcwd()}/downloads/mountains.jpg')
time.sleep(3)
