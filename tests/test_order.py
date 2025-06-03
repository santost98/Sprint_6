import allure
import pytest
from pages.home_page import HomePage
from pages.order_form_page import OrderFormPage
from data import ORDER_DATA

@allure.feature('Заказ самоката')
class TestOrder:
    @pytest.mark.parametrize("order_data,button_method", [
        (data, "click_order_button_header") for data in ORDER_DATA
    ] + [
        (data, "click_order_button_body") for data in ORDER_DATA
    ])
    @allure.title('Тест заказа самоката')
    @allure.description('Проверяем полный флоу заказа самоката')
    def test_order_scooter(self, driver, order_data, button_method):
        home_page = HomePage(driver)
        order_form_page = OrderFormPage(driver)

        with allure.step('Принимаем куки'):
            home_page.accept_cookies()

        with allure.step('Кликаем на кнопку "Заказать"'):
            getattr(home_page, button_method)()

        with allure.step('Заполняем первую страницу формы'):
            order_form_page.fill_first_name(order_data["name"])
            order_form_page.fill_last_name(order_data["surname"])
            order_form_page.fill_address(order_data["address"])
            order_form_page.select_metro_station(order_data["metro_station"])
            order_form_page.fill_phone_number(order_data["phone"])
            order_form_page.click_continue_button()

        with allure.step('Заполняем вторую страницу формы'):
            order_form_page.fill_rental_date(order_data["date"])
            order_form_page.select_rental_duration(order_data["duration"])
            order_form_page.choose_scooter_color(order_data["color"])
            order_form_page.fill_comment(order_data["comment"])
            order_form_page.click_order_button()

        with allure.step('Подтверждаем заказ'):
            order_form_page.confirm_order()

        with allure.step('Проверяем успешное создание заказа'):
            assert order_form_page.check_order_complete(), 'Сообщение об успешном заказе не отображается'
