from header import *
from custom_utils import *

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "first_block .form-control.first")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CLASS_NAME, "first_block .form-control.second")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "first_block .form-control.third")
    input3.send_keys("test@test.com")

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
    print(Fore.RED + f"ЭРРОР НАХУЙ!!!: {str(e)}")
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(3)
    browser.quit()
