from .base_page import BasePage
from locators.order_form_locators import OrderFormLocators
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderFormPage(BasePage):
    @allure.step('Заполняем поле имени значением {first_name}')
    def fill_first_name(self, first_name):
        self.input_text(OrderFormLocators.FIRST_NAME_FIELD, first_name)

    @allure.step('Заполняем поле фамилии значением {last_name}')
    def fill_last_name(self, last_name):
        self.input_text(OrderFormLocators.LAST_NAME_FIELD, last_name)

    @allure.step('Заполняем поле адреса значением {address}')
    def fill_address(self, address):
        self.input_text(OrderFormLocators.ADDRESS_FIELD, address)

    @allure.step('Выбираем станцию метро {station}')
    def select_metro_station(self, station):
        self.click_element(OrderFormLocators.METRO_STATION_FIELD)
        self.input_text(OrderFormLocators.METRO_STATION_FIELD, station)
        self.click_element(OrderFormLocators.SELECTED_STATION)

    @allure.step('Заполняем поле телефона значением {phone}')
    def fill_phone_number(self, phone):
        self.input_text(OrderFormLocators.PHONE_NUMBER_FIELD, phone)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_continue_button(self):
        self.wait.until(EC.element_to_be_clickable(OrderFormLocators.CONTINUE_BUTTON))
        self.click_element(OrderFormLocators.CONTINUE_BUTTON)

    @allure.step('Заполняем дату доставки значением {date}')
    def fill_rental_date(self, date):
        self.input_text(OrderFormLocators.RENTAL_DATE_FIELD, date)

    @allure.step('Выбираем срок аренды')
    def select_rental_duration(self, duration):
        # Сначала закрываем календарь, если он открыт
        try:
            calendar = self.driver.find_element(By.CLASS_NAME, "react-datepicker__current-month")
            if calendar.is_displayed():
                # Кликаем в любое место страницы, чтобы закрыть календарь
                self.driver.find_element(By.TAG_NAME, "body").click()
                # Ждем, пока календарь исчезнет
                WebDriverWait(self.driver, 10).until_not(
                    EC.visibility_of_element_located((By.CLASS_NAME, "react-datepicker__current-month"))
                )
        except:
            pass
        
        # Ждем, пока поле выбора срока аренды станет кликабельным
        self.wait.until(EC.element_to_be_clickable(OrderFormLocators.RENTAL_DURATION_FIELD))
        
        # Скроллим до элемента
        element = self.driver.find_element(*OrderFormLocators.RENTAL_DURATION_FIELD)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        
        # Теперь кликаем на поле выбора срока аренды
        self.click_element(OrderFormLocators.RENTAL_DURATION_FIELD)
        
        # Ждем появления опций и выбираем нужный срок
        duration_option = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{duration}']")
        self.wait.until(EC.element_to_be_clickable(duration_option))
        self.click_element(duration_option)

    @allure.step('Выбираем цвет самоката')
    def choose_scooter_color(self, color):
        if color == 'black' or color == 'чёрный':
            self.click_element(OrderFormLocators.CHECKBOX_BLACK)
        elif color == 'grey' or color == 'серый':
            self.click_element(OrderFormLocators.CHECKBOX_GREY)

    @allure.step('Заполняем комментарий для курьера значением {comment}')
    def fill_comment(self, comment):
        self.input_text(OrderFormLocators.COMMENT_FIELD, comment)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order_button(self):
        # Скроллим до кнопки
        element = self.driver.find_element(*OrderFormLocators.ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.wait.until(EC.element_to_be_clickable(OrderFormLocators.ORDER_BUTTON), message='Кнопка Заказать не кликабельна')
        self.click_element(OrderFormLocators.ORDER_BUTTON, timeout=20)

    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        # Ждём появления окна подтверждения
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Order_Modal__YZ-d3"))
        )
        # Ждём, пока кнопка "Да" станет кликабельной
        self.wait.until(
            EC.element_to_be_clickable(OrderFormLocators.YES_BUTTON_POP_UP_CONFIRM_ORDER)
        )
        self.click_element(OrderFormLocators.YES_BUTTON_POP_UP_CONFIRM_ORDER)

    @allure.step('Проверяем, что заказ оформлен')
    def check_order_complete(self):
        self.wait.until(
            EC.visibility_of_element_located(OrderFormLocators.POP_UP_COMPLETE_ORDER)
        )
        return self.find_element(OrderFormLocators.POP_UP_COMPLETE_ORDER).is_displayed()