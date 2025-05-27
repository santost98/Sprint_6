import allure
import pytest
from pages.home_page import HomePage
from data import FAQ_ANSWERS

@allure.feature('FAQ')
class TestFAQ:
    @pytest.mark.parametrize("question_index", range(8))
    @allure.title('Тест вопроса FAQ')
    @allure.description('Проверяем, что текст вопроса появляется при клике')
    def test_faq_question(self, driver, question_index):
        home_page = HomePage(driver)
        
        with allure.step('Принимаем куки'):
            home_page.accept_cookies()

        with allure.step(f'Кликаем на вопрос {question_index + 1}'):
            home_page.click_faq_question(question_index)

        with allure.step('Проверяем текст ответа'):
            actual_answer = home_page.get_faq_answer(question_index)
            assert actual_answer == FAQ_ANSWERS[question_index], \
                f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[question_index]}\nПолучено: {actual_answer}'