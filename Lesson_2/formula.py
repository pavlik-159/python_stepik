from header import *
from custom_utils import *


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # try/finnaly - конструкция для того чтобы закрыть окно браузера даже если в середине теста упадет с ошибкой
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option1.click()

    option2 = browser.find_element(By.ID, "robotCheckbox")
    option2.click()

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
