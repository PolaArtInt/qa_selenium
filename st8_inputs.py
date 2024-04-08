from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://demoqa.com/text-box'

driver.get(url)

email_field = driver.find_element('xpath', '//input[@id="userEmail"]')
email_field.send_keys('john.smith@email.com')  # ввод значения в поле
time.sleep(2)

email_field_value = email_field.get_attribute('value')  # запись введённого значения
print(email_field_value)
time.sleep(2)

email_field.clear()  # очистка инпута
assert email_field.get_attribute("value") == ''  # проверяем, что инпут пустой
time.sleep(2)

email_field.send_keys('jane.smith@email.com')  # ввод другого значения
print(email_field.get_attribute('value'))  # значение перезаписалось
time.sleep(2)

assert email_field.get_attribute('value') == 'jane.smith@email.com', 'Wrong email'
time.sleep(2)

# получение других атрибутов:
# class, href, data-component-name etc.

# practice:
# Форма - https://demoqa.com/automation-practice-form
# Клавиатура - http://the-internet.herokuapp.com/key_presses?
# Клипборд - https://clipboardjs.com/

