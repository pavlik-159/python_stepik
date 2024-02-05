import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/simple_form_find_task.html")
    button = browser.find_element(By.ID, "submit_button")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
