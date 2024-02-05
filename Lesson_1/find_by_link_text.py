import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/find_link_text"
result = str(math.ceil(math.pow(math.pi, math.e) * 10000))

# try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой

try:

    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    link = browser.find_element(By.LINK_TEXT, result)
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()




finally:
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
#ОБЯЗАТЕЛЬНО ОСТАВЬ ПУСТУЮ СТРОКУ В КОНЦЕ ФАЙЛА !!!!!!!