from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config import Config
import allure
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)

    @allure.step('Находим элемент по локатору {locator}')
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

    @allure.step('Находим все элементы по локатору {locator}')
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step('Кликаем по элементу {locator}')
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

    @allure.step('Вводим текст "{text}" в поле {locator}')
    def input_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Получаем текст элемента {locator}')
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

    @allure.step('Скроллим страницу до элемента {locator}')
    def scroll_to_element(self, locator):
        """
        Скроллит страницу до элемента
        :param locator: локатор элемента
        """
        element = self.find_element(locator)
        self.scroll_into_view(element)

    @allure.step('Скроллим элемент в область видимости')
    def scroll_into_view(self, element):
        """
        Скроллит элемент в область видимости
        :param element: элемент для скролла
        """
        self.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидаем, пока элемент {locator} станет кликабельным')
    def wait_for_element_clickable(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет кликабельным
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step('Ожидаем, пока элемент {locator} станет видимым')
    def wait_for_element_visible(self, locator, timeout=10):
        """
        Ожидает, пока элемент станет видимым
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидаем, пока элемент {locator} исчезнет')
    def wait_for_element_not_visible(self, locator, timeout=10):
        """
        Ожидает, пока элемент исчезнет
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        """
        return WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Выполняем JavaScript код: {script}')
    def execute_script(self, script, *args):
        """
        Выполняет JavaScript код
        :param script: JavaScript код
        :param args: аргументы для скрипта
        """
        return self.driver.execute_script(script, *args)

    @allure.step('Переключаемся на окно с индексом {index}')
    def switch_to_window(self, index):
        """
        Переключает драйвер на окно с заданным индексом
        :param index: индекс окна
        """
        self.driver.switch_to.window(self.driver.window_handles[index])

    @allure.step('Получаем текущий URL страницы')
    def get_current_url(self):
        """
        Возвращает текущий URL страницы
        :return: str
        """
        return self.driver.current_url

    @allure.step('Устанавливаем неявное ожидание {timeout} секунд')
    def set_implicit_wait(self, timeout):
        """
        Устанавливает неявное ожидание для драйвера
        :param timeout: время ожидания в секундах
        """
        self.driver.implicitly_wait(timeout)

    @allure.step('Получаем список дескрипторов окон')
    def get_window_handles(self):
        """
        Возвращает список дескрипторов окон
        :return: list
        """
        return self.driver.window_handles

    @allure.step('Ожидаем появления нового окна')
    def wait_for_new_window(self, timeout=20):
        """
        Ожидает появления нового окна
        :param timeout: время ожидания в секундах
        :return: bool
        """
        initial_handles = self.get_window_handles()
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            current_handles = self.get_window_handles()
            if len(current_handles) > len(initial_handles):
                time.sleep(3)
                return True
            time.sleep(0.5)
            
        return False

    @allure.step('Ожидаем изменения URL с {current_url}')
    def wait_for_url_change(self, current_url, timeout=20):
        """
        Ожидает изменения URL
        :param current_url: текущий URL
        :param timeout: время ожидания в секундах
        :return: str
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            url = self.get_current_url()
            if url != current_url:
                return url
            time.sleep(0.5)
        return self.get_current_url()

    @allure.step('Ожидаем, пока URL не станет отличным от about:blank')
    def wait_for_url_not_blank(self, timeout=20):
        """
        Ожидает, пока URL не станет отличным от about:blank
        :param timeout: время ожидания в секундах
        """
        return self.wait_for_url_change("about:blank", timeout)

    @allure.step('Проверяем переход по логотипу {logo_type}')
    def check_redirect(self, logo_type):
        if logo_type == "yandex":
            self.switch_to_window(1)
            self.set_implicit_wait(20)
            self.wait_for_url_not_blank()
            url = self.get_current_url()
            assert "dzen.ru" in url, \
                f'Переход по логотипу Яндекса не работает. URL: {url}'

    @allure.step('Проверяем, что элемент {locator} отображается')
    def is_element_displayed(self, locator, timeout=10):
        """
        Проверяет, что элемент отображается на странице
        :param locator: локатор элемента
        :param timeout: время ожидания в секундах
        :return: bool
        """
        try:
            element = self.find_element(locator, timeout)
            return element.is_displayed()
        except:
            return False