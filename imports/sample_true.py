from header import *
from custom_utils import *

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = ""
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)  # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.get(link)




    print(Fore.GREEN + "Тест успешно пройден")

except Exception as e:
    # Если произошла ошибка, выводим только сообщение об ошибке
    print(Fore.RED + "ЭРРОР НАХУЙ!!!: " + str(e))
    error_flag = True

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(7)
    browser.quit()
