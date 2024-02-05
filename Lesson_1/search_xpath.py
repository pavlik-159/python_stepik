import time
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/find_xpath_form"
# try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[3]/input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.XPATH, "/html/body/div[1]/form/div[6]/button[3]")
    button.click()





finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()
#ОБЯЗАТЕЛЬНО ОСТАВЬ ПУСТУЮ СТРОКУ В КОНЦЕ ФАЙЛА !!!!!!!
