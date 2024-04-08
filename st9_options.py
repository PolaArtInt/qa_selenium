import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Опции браузера
options = webdriver.ChromeOptions()

# типы стратегии загрузки:
# normal - используется по дефолту и ожидает загрузки всех ресурсов (картинки, js-код, шрифты и т.д)
# eager - ожидает только загрузку DOM, но при этом картинки и прочее может до сих пор грузиться
# none - ничего не ждет
options.page_load_strategy = 'normal'

# options.add_argument("--headless")  # браузер работает в фоновом режиме
options.add_argument("--incognito")  # вход в режиме инкогнито
options.add_argument("--ignore-certificate-errors")  # игнорирование ошибок сертификатов
options.add_argument("--window-size=1920,1080")  # размер окна браузера
options.add_argument("--disable-cache")  # отключает кэширование в браузере

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(5)

url_1 = 'https://google.com'
url_2 = 'https://whatismyipaddress.com/'

driver.get(url_1)
print(driver.title)

driver.get(url_2)
time.sleep(2)
print(driver.title)
driver.quit()
