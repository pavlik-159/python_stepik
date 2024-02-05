from selenium import webdriver
from selenium.webdriver.common.by import By
from imports.custom_utils import find_element_and_send_keys
from colorama import init, Fore

# Инициализация colorama
init(autoreset=True)

link = "http://suninjuly.github.io/registration1.html"


# Пример использования функции в вашем тесте
try:
    browser = webdriver.Chrome()
    browser.get(link)

    find_element_and_send_keys(browser, "tag", "input", "Ivan")
    find_element_and_send_keys(browser, "class", "form-control.second", "Petrov")
    find_element_and_send_keys(browser, "class", "form-control.third1", "test@test.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(3)

    # Проверяем успешность выполнения теста
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

    print(Fore.GREEN + "Тест успешно пройден")

except Exception as e:
    # Если произошла ошибка, выводим только сообщение об ошибке
    print(Fore.RED + f"Ошибка: {str(e)}")

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
