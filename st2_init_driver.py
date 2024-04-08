# Chromedriver:
import time
from selenium import webdriver

driver = webdriver.Chrome()
time.sleep(3)
# работает!

# or:
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# or:
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# service = Service(ChromeDriverManager(driver_version="114.0.5735.16").install())
# driver = webdriver.Chrome(service=service)

# for Firefox:
# Selenium Manager:
# from selenium import webdriver
# driver = webdriver.Firefox()
# WebDriverManager:
# from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.firefox.service import Service
# service = Service(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service)
