from header import *
from custom_utils import *

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Получаем значения чисел из элементов с id "sum1" и "sum2"
    x = int(browser.find_element(By.ID, "num1").text)
    y = int(browser.find_element(By.ID, "num2").text)
    # Вычисляем результат
    result = calc_sum(x, y)
    browser.find_element(By.ID, "dropdown").click()
    # ищем и кликаем на элемент значение тега которого равно результату нашей формулы
    browser.find_element(By.CSS_SELECTOR, f"[value='{result}']").click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
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
