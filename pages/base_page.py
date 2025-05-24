from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    def find_element(self, locator, timeout=10):
        """
        Находит элемент с явным ожиданием
        :param locator: локатор элемента
        :return: найденный элемент
        """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise NoSuchElementException(f"Элемент {locator} не найден")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator, timeout=10):
        """
        Кликает по элементу с явным ожиданием
        :param locator: локатор элемента
        """
        try:
            element = self.find_element(locator, timeout)
            element.click()
        except TimeoutException:
            raise NoSuchElementException(f"Не удалось кликнуть по элементу {locator}")

    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Получает текст элемента
        :param locator: локатор элемента
        :return: текст элемента
        """
        try:
            element = self.find_element(locator)
            return element.text
        except TimeoutException:
            raise NoSuchElementException(f"Не удалось получить текст элемента {locator}")