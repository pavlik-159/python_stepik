from header import *
from custom_utils import *

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    # Используем явное ожидание для дожидания появления текста "time is up :"
    wait = WebDriverWait(browser, 11)  # Максимальное время ожидания появления текста в секундах
    # сам текст появление которого мы ждем
    element = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='countdown'][contains(text(),'time is up :')]")))
    #ищем кнопку и проверяем что по истечении таймера кнопка сабмит задизейблена
    but_sub = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    but_disabled = "true" in but_sub.get_attribute("class")
    assert not but_disabled

    print(Fore.GREEN + "Тест успешно пройден")

except Exception as e:
    # Если произошла ошибка, выводим только сообщение об ошибке
    print(Fore.RED + "ЭРРОР НАХУЙ!!!: " + str(e))
    error_flag = True

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(7)
    browser.quit()
