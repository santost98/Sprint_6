from selenium.webdriver.common.by import By

class OrderFormLocators:
    # Первая страница формы
    FIRST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_FIELD = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    SELECTED_STATION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    CONTINUE_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница формы
    RENTAL_DATE_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_DURATION_FIELD = (By.XPATH, "//div[contains(@class, 'Dropdown-control')]")
    CHECKBOX_BLACK = (By.ID, "black")
    CHECKBOX_GREY = (By.ID, "grey")
    COMMENT_FIELD = (By.XPATH, "//textarea[contains(@placeholder, 'Комментарий для курьера')] | //input[contains(@placeholder, 'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
    YES_BUTTON_POP_UP_CONFIRM_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]//button[text()='Да']")
    POP_UP_COMPLETE_ORDER = (By.XPATH, "//div[contains(@class, 'Order_Modal__YZ-d3')]//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]") 