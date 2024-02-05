import time

from header import *
from custom_utils import *

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary")
    button.click()
    # Получаем список всех открытых окон
    window_handles = browser.window_handles
    new_window_handle = window_handles[1]
    browser.switch_to.window(new_window_handle)
    time.sleep(1)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Вычисляем результат
    result = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button.click()






    print(Fore.GREEN + "Тест успешно пройден")

except Exception as e:
    # Если произошла ошибка, выводим только сообщение об ошибке
    print(Fore.RED + "ЭРРОР НАХУЙ!!!: " + str(e))
    error_flag = True

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(7)
    browser.quit()
