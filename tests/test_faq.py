import allure
import pytest
from pages.home_page import HomePage
from data import FAQ_ANSWERS

@allure.title('Тест первого вопроса FAQ')
@allure.description('Проверяем, что текст первого вопроса появляется при клике')
def test_faq_first_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на первый вопрос')
    def click_first_question():
        home_page.click_faq_question(0)
    click_first_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(0)
        assert actual_answer == FAQ_ANSWERS[0], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[0]}\nПолучено: {actual_answer}'
    check_answer()

@allure.title('Тест второго вопроса FAQ')
@allure.description('Проверяем, что текст второго вопроса появляется при клике')
def test_faq_second_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на второй вопрос')
    def click_second_question():
        home_page.click_faq_question(1)
    click_second_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(1)
        assert actual_answer == FAQ_ANSWERS[1], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[1]}\nПолучено: {actual_answer}'
    check_answer()

@allure.title('Тест третьего вопроса FAQ')
@allure.description('Проверяем, что текст третьего вопроса появляется при клике')
def test_faq_third_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на третий вопрос')
    def click_third_question():
        home_page.click_faq_question(2)
    click_third_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(2)
        assert actual_answer == FAQ_ANSWERS[2], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[2]}\nПолучено: {actual_answer}'
    check_answer()

@allure.title('Тест четвертого вопроса FAQ')
@allure.description('Проверяем, что текст четвертого вопроса появляется при клике')
def test_faq_fourth_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на четвертый вопрос')
    def click_fourth_question():
        home_page.click_faq_question(3)
    click_fourth_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(3)
        assert actual_answer == FAQ_ANSWERS[3], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[3]}\nПолучено: {actual_answer}'
    check_answer()

@allure.title('Тест пятого вопроса FAQ')
@allure.description('Проверяем, что текст пятого вопроса появляется при клике')
def test_faq_fifth_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на пятый вопрос')
    def click_fifth_question():
        home_page.click_faq_question(4)
    click_fifth_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(4)
        assert actual_answer == FAQ_ANSWERS[4], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[4]}\nПолучено: {actual_answer}'
    check_answer()

@allure.title('Тест шестого вопроса FAQ')
@allure.description('Проверяем, что текст шестого вопроса появляется при клике')
def test_faq_sixth_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на шестой вопрос')
    def click_sixth_question():
        home_page.click_faq_question(5)
    click_sixth_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(5)
        assert actual_answer == FAQ_ANSWERS[5], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[5]}\nПолучено: {actual_answer}'
    check_answer()

@allure.title('Тест седьмого вопроса FAQ')
@allure.description('Проверяем, что текст седьмого вопроса появляется при клике')
def test_faq_seventh_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на седьмой вопрос')
    def click_seventh_question():
        home_page.click_faq_question(6)
    click_seventh_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(6)
        assert actual_answer == FAQ_ANSWERS[6], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[6]}\nПолучено: {actual_answer}'
    check_answer()

@allure.title('Тест восьмого вопроса FAQ')
@allure.description('Проверяем, что текст восьмого вопроса появляется при клике')
def test_faq_eighth_question(driver):
    home_page = HomePage(driver)
    
    @allure.step('Принимаем куки')
    def accept_cookies():
        home_page.accept_cookies()
    accept_cookies()

    @allure.step('Кликаем на восьмой вопрос')
    def click_eighth_question():
        home_page.click_faq_question(7)
    click_eighth_question()

    @allure.step('Проверяем текст ответа')
    def check_answer():
        actual_answer = home_page.get_faq_answer(7)
        assert actual_answer == FAQ_ANSWERS[7], \
            f'Текст ответа не соответствует ожидаемому.\nОжидалось: {FAQ_ANSWERS[7]}\nПолучено: {actual_answer}'
    check_answer()