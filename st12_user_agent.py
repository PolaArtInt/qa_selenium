import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

user_agents_list = 'https://useragents.ru/stable.html'
user_agents_mobile = 'https://deviceatlas.com/blog/mobile-browser-user-agent-strings'


@pytest.fixture()
def human_driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko)"
                         "Chrome/114.0.0.0 Mobile Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def not_human_driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


def test_human(human_driver):
    human_driver.get('https://facebook.com/')
    # human_driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    # human_driver.save_screenshot('human.png')
    human_driver.save_screenshot('human1.png')


def test_not_human(not_human_driver):
    not_human_driver.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    # not_human_driver.save_screenshot('not_human.png')
    not_human_driver.save_screenshot('not_human1.png')
