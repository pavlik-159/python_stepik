from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    # Находим элементы формы
    input1 = browser.find_element(By.CSS_SELECTOR, "input[type='text'][name='first_name']")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[type='text'][name='last_name']")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[type='text'][name='email']")
    input4 = browser.find_element(By.CSS_SELECTOR, "input[type='text'][name='phone']")
    input5 = browser.find_element(By.CSS_SELECTOR, "input[type='text'][name='address']")

    # Вводим данные
    input1.send_keys("Ivan")
    input2.send_keys("Petrov")
    input3.send_keys("email@example.com")
    input4.send_keys("+79123456789")
    input5.send_keys("ул. Садовая, д. 1")

    # Кликаем по кнопке
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла