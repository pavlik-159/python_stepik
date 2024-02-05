# custom_utils.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from colorama import Fore

def find_element_and_send_keys(browser, method, selector, keys):
    try:
        if method == "tag":
            element = browser.find_element(By.TAG_NAME, selector)
        elif method == "class":
            element = browser.find_element(By.CLASS_NAME, selector)
        elif method == "id":
            element = browser.find_element(By.ID, selector)
        elif method == "name":
            element = browser.find_element(By.NAME, selector)
        elif method == "xpath":
            element = browser.find_element(By.XPATH, selector)
        elif method == "css":
            element = browser.find_element(By.CSS_SELECTOR, selector)
        elif method == "link_text":
            element = browser.find_element(By.LINK_TEXT, selector)
        elif method == "partial_link_text":
            element = browser.find_element(By.PARTIAL_LINK_TEXT, selector)
        else:
            raise ValueError(f"Неизвестный метод поиска: {method}")

        element.send_keys(keys)

    except NoSuchElementException:
        raise NoSuchElementException(f"Элемент с {method} селектором '{selector}' не найден")

# Можно добавить дополнительные функции или классы в этот файл, если необходимо
