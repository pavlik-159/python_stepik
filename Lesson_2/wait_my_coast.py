from header import *
from custom_utils import *

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    book_button = browser.find_element(By.ID, "book")
    book_button.click()
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    # Вычисляем результат
    result = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))
    button = browser.find_element(By.ID, "solve")
    button.click()


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
