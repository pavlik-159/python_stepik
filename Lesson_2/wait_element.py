from header import *
from custom_utils import *

try:  # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Используем явное ожидание для дожидания появления текста "time is up :"
    wait = WebDriverWait(browser, 1)  # Максимальное время ожидания появления текста в секундах
    # сам текст появление которого мы ждем
    element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//span[@id='countdown'][contains(text(),'time is up :')]")))


    print(Fore.GREEN + "Тест успешно пройден")

except Exception as e:
    # Если произошла ошибка, выводим только сообщение об ошибке
    print(Fore.RED + "ЭРРОР НАХУЙ!!!: " + str(e))
    error_flag = True

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(3)
    browser.quit()
