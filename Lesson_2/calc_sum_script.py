from header import *
from custom_utils import *

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Получаем значение числа из элемента с id "input_value"
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Вычисляем результат
    result = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()

    option2 = browser.find_element(By.ID, "robotCheckbox")
    option2.click()

    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
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
