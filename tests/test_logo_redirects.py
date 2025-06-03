import allure
import pytest
from pages.home_page import HomePage
from config import Config

@allure.feature('Переходы по логотипам')
class TestLogoRedirects:
    @allure.title('Тест перехода по логотипу Яндекса')
    @allure.description('Проверяем корректность перехода по логотипу Яндекса')
    def test_yandex_logo_redirect(self, driver):
        home_page = HomePage(driver)

        with allure.step('Принимаем куки'):
            home_page.accept_cookies()

        with allure.step('Кликаем на логотип Яндекса'):
            home_page.click_logo_yandex()

        with allure.step('Проверяем переход'):
            home_page.check_redirect("yandex")

    @allure.title('Тест перехода по логотипу Самоката')
    @allure.description('Проверяем корректность перехода по логотипу Самоката')
    def test_samokat_logo_redirect(self, driver):
        home_page = HomePage(driver)

        with allure.step('Принимаем куки'):
            home_page.accept_cookies()

        with allure.step('Кликаем на логотип Самоката'):
            home_page.click_logo_samokat()

        with allure.step('Проверяем переход на главную страницу'):
            assert Config.BASE_URL in home_page.get_current_url(), \
                f'Переход по логотипу Самоката не работает. URL: {home_page.get_current_url()}'