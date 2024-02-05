from header import *
from custom_utils import *

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ждем появления кнопки с id=verify
    wait = WebDriverWait(browser, 10)
    verify_button = wait.until(EC.presence_of_element_located((By.ID, "verify")))
    button = browser.find_element(By.ID, "verify")
    button.click()
    # Провоеряем наличие текста по id
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    print(Fore.GREEN + "Тест успешно пройден")

except Exception as e:
    # Если произошла ошибка, выводим только сообщение об ошибке
    print(Fore.RED + "ЭРРОР НАХУЙ!!!: " + str(e))
    error_flag = True

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(7)
    browser.quit()
