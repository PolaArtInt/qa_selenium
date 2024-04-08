from selenium import webdriver
import time

driver = webdriver.Chrome()

url_1 = 'https://demoqa.com/text-box'
url_2 = 'https://the-internet.herokuapp.com/status_codes'


# Task 1:
# Заполнить все текстовые поля данными (почистить поля перед заполнением).
# Проверить, что данные действительно введены, используя get_attribute() и assert.
def test_fill_all_inputs():
    driver.get(url_1)
    driver.maximize_window()

    user_name_field = driver.find_element('xpath', '//input[@id="userName"]')
    email_field = driver.find_element('xpath', '//input[@id="userEmail"]')
    curr_address_field = driver.find_element('xpath', '//textarea[@id="currentAddress"]')
    perm_address_field = driver.find_element('xpath', '//textarea[@id="permanentAddress"]')

    fields = {
        user_name_field: 'Jane',
        email_field: 'Smith',
        curr_address_field: '6629 Lomas Blvd NE\nNew York',
        perm_address_field: '621 E Pine St\nCalifornia'
    }
    time.sleep(2)

    for field, val in fields.items():
        field.clear()
        assert field.get_attribute('value') == '', 'Field is not empty'
        field.send_keys(val)
        assert val in field.get_attribute('value'), 'Field is not filled'
        print(f'\n{val}')
    time.sleep(2)


# Task 2:
# Прокликать все ссылки со статус - кодами на странице, используя алгоритм перебора элементов.
# После каждого клика возвращаться на стартовую страницу.
def test_status_links_click():
    driver.get(url_2)
    time.sleep(2)

    links = [driver.find_element('xpath', '(//a[contains(@href, "status_codes")])[1]'),
             driver.find_element('xpath', '(//a[contains(@href, "status_codes")])[2]'),
             driver.find_element('xpath', '(//a[contains(@href, "status_codes")])[3]'),
             driver.find_element('xpath', '(//a[contains(@href, "status_codes")])[4]')]
    time.sleep(2)

    for link in links:
        print(f'\n{link.text}')
        link.click()
        time.sleep(2)
        assert driver.current_url != url_2, 'Wrong url'
        driver.back()
        assert driver.current_url == url_2, 'Wrong url'
        time.sleep(2)

    assert driver.current_url == url_2, 'Wrong url'
    time.sleep(2)
    driver.quit()

