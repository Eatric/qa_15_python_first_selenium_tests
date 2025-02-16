import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from locators import Locators


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(Data.MESTO_URL)

    yield chrome_driver

    chrome_driver.quit()

@pytest.fixture(scope='function')
def loggined_driver(driver):
    email_input = driver.find_element(*Locators.MESTO_EMAIL_INPUT)
    email_input.send_keys(Data.MESTO_LOGIN)

    password_input = driver.find_element(*Locators.MESTO_PASSWORD_INPUT)
    password_input.send_keys(Data.MESTO_PASSWORD)

    enter_button = driver.find_element(*Locators.MESTO_LOGIN_BUTTON)
    enter_button.click()

    WebDriverWait(driver, Data.WAIT_TIME).until(
        EC.text_to_be_present_in_element(Locators.MESTO_PROFILE_TITLE, Data.MESTO_PROFILE_TITLE_TEXT))

    yield driver