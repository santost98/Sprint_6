from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
import allure

class HomePage(BasePage):
    @allure.step('Кликаем на кнопку "Заказать" в хедере')
    def click_order_button_header(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_HEADER)

    @allure.step('Кликаем на кнопку "Заказать" в теле страницы')
    def click_order_button_body(self):
        # Скроллим до кнопки перед кликом
        element = self.driver.find_element(*HomePageLocators.ORDER_BUTTON_BODY)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click_element(HomePageLocators.ORDER_BUTTON_BODY)

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        self.click_element(HomePageLocators.COOKIE_BUTTON)

    @allure.step('Кликаем на вопрос FAQ с индексом {index}')
    def click_faq_question(self, index):
        question_locator = getattr(HomePageLocators, f'ACCORDION_BUTTON_FAQ_{index + 1}')
        self.click_element(question_locator)

    @allure.step('Получаем текст ответа FAQ с индексом {index}')
    def get_faq_answer(self, index):
        answer_locator = getattr(HomePageLocators, f'ANSWER_FAQ_{index + 1}')
        return self.get_text(answer_locator)

    @allure.step('Кликаем на логотип Яндекса')
    def click_logo_yandex(self):
        self.click_element(HomePageLocators.LOGO_YANDEX)

    @allure.step('Кликаем на логотип Самоката')
    def click_logo_samokat(self):
        self.click_element(HomePageLocators.LOGO_SAMOKAT)