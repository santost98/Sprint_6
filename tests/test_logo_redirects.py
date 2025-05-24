import allure
import pytest
from pages.home_page import HomePage
from config import Config
from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.parametrize("logo_type,expected_url", [
    ("yandex", Config.DZEN_URL),
    ("samokat", Config.BASE_URL)
])
@allure.title('Тест перехода по логотипам')
@allure.description('Проверяем корректность переходов по логотипам')
def test_logo_redirects(driver, logo_type, expected_url):
    home_page = HomePage(driver)

    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step(f'Кликаем на логотип {"Яндекса" if logo_type == "yandex" else "Самоката"}')
    def click_logo():
        if logo_type == "yandex":
            home_page.click_logo_yandex()
        else:
            home_page.click_logo_samokat()
    click_logo()

    @allure.step('Проверяем переход')
    def check_redirect():
        if logo_type == "yandex":
            driver.switch_to.window(driver.window_handles[1])
            driver.implicitly_wait(20)
            WebDriverWait(driver, 20).until(
                lambda d: d.current_url != "about:blank"
            )
            assert "dzen.ru" in driver.current_url, \
                f'Переход по логотипу Яндекса не работает. URL: {driver.current_url}'
        else:
            assert expected_url in driver.current_url, \
                f'Переход по логотипу Самоката не работает. URL: {driver.current_url}'
    check_redirect()