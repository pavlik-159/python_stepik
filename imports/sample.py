import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from colorama import init, Fore
init(autoreset=True) # Инициализация colorama

try: # try/finnaly - конструкция для того что бы закрыть окно браузера даже если в середине тест упадет с ошибкой
    link = ""
    browser = webdriver.Chrome()
    browser.get(link)










except Exception as e:
    # Если произошла ошибка, выводим только сообщение об ошибке
    print(Fore.RED + f"ЭРРОР НАХУЙ!!!: {str(e)}")
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    print(Fore.GREEN + "Тест успешно пройден")
    browser.quit()
