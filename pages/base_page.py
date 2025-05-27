from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import Config
import allure

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

    def scroll_to_element(self, locator):
        """
        Скроллит страницу до элемента
        :param locator: локатор элемента
        """
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_element_clickable(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет кликабельным
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_visible(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет видимым
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_not_visible(self, locator, timeout=10):
        """
        Ожидает, пока элемент исчезнет
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        """
        return WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of_element_located(locator)
        )

    def execute_script(self, script, *args):
        """
        Выполняет JavaScript код
        :param script: JavaScript код
        :param args: аргументы для скрипта
        """
        return self.driver.execute_script(script, *args)

    def switch_to_window(self, index):
        """
        Переключает драйвер на окно с заданным индексом
        :param index: индекс окна
        """
        self.driver.switch_to.window(self.driver.window_handles[index])

    def get_current_url(self):
        """
        Возвращает текущий URL страницы
        :return: str
        """
        return self.driver.current_url

    def set_implicit_wait(self, timeout):
        """
        Устанавливает неявное ожидание для драйвера
        :param timeout: время ожидания в секундах
        """
        self.driver.implicitly_wait(timeout)