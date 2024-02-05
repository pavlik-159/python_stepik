import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/huge_form.html"
# try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, '.first_block input')
    for element in elements:
        element.send_keys("pasha")
    time.sleep(5)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()





finally:
    # закрываем браузер после всех манипуляций
    time.sleep(15)
    browser.quit()
#ОБЯЗАТЕЛЬНО ОСТАВЬ ПУСТУЮ СТРОКУ В КОНЦЕ ФАЙЛА !!!!!!!