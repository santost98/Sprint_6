import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from config import Config

@pytest.fixture(scope='function')
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.get(Config.BASE_URL)
    yield driver
    driver.quit()