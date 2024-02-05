from header import *
from custom_utils import *

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://suninjuly.github.io/wait1.html"
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get(link)
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
