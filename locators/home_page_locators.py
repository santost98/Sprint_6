from selenium.webdriver.common.by import By

class HomePageLocators:
    # Кнопки заказа
    ORDER_BUTTON_HEADER = (By.CSS_SELECTOR, "button.Button_Button__ra12g:not(.Button_Middle__1CSJM)")
    ORDER_BUTTON_BODY = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    
    # Логотипы
    LOGO_YANDEX = (By.CSS_SELECTOR, "img[alt='Yandex']")
    LOGO_SAMOKAT = (By.CSS_SELECTOR, "img[alt='Scooter']")
    
    # FAQ
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "div.accordion__button")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "div.accordion__panel")
    
    # Куки
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")

    # Блок "Как это работает"
    HOW_IT_WORKS_BLOCK = (By.CSS_SELECTOR, 'div:has-text("Как это работает")')

    # Блок FAQ
    ACCORDION_BUTTON_FAQ_1 = (By.ID, 'accordion__heading-0')
    ANSWER_FAQ_1 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-0"]:not([hidden]) p')
    ACCORDION_BUTTON_FAQ_2 = (By.ID, 'accordion__heading-1')
    ANSWER_FAQ_2 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-1"]:not([hidden]) p')
    ACCORDION_BUTTON_FAQ_3 = (By.ID, 'accordion__heading-2')
    ANSWER_FAQ_3 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-2"]:not([hidden]) p')
    ACCORDION_BUTTON_FAQ_4 = (By.ID, 'accordion__heading-3')
    ANSWER_FAQ_4 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-3"]:not([hidden]) p')
    ACCORDION_BUTTON_FAQ_5 = (By.ID, 'accordion__heading-4')
    ANSWER_FAQ_5 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-4"]:not([hidden]) p')
    ACCORDION_BUTTON_FAQ_6 = (By.ID, 'accordion__heading-5')
    ANSWER_FAQ_6 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-5"]:not([hidden]) p')
    ACCORDION_BUTTON_FAQ_7 = (By.ID, 'accordion__heading-6')
    ANSWER_FAQ_7 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-6"]:not([hidden]) p')
    ACCORDION_BUTTON_FAQ_8 = (By.ID, 'accordion__heading-7')
    ANSWER_FAQ_8 = (By.CSS_SELECTOR, 'div[aria-labelledby="accordion__heading-7"]:not([hidden]) p')