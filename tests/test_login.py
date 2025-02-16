from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import Data
from helper import Helper
from locators import Locators


class TestLogin:
    def test_login(self, driver):
        email_input = driver.find_element(*Locators.MESTO_EMAIL_INPUT)
        email_input.send_keys(Data.MESTO_LOGIN)

        password_input = driver.find_element(*Locators.MESTO_PASSWORD_INPUT)
        password_input.send_keys(Data.MESTO_PASSWORD)

        enter_button = driver.find_element(*Locators.MESTO_LOGIN_BUTTON)
        enter_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.text_to_be_present_in_element(Locators.MESTO_PROFILE_TITLE, Data.MESTO_PROFILE_TITLE_TEXT))

        profile_title = driver.find_element(*Locators.MESTO_PROFILE_TITLE)

        assert profile_title.is_displayed() and profile_title.text == Data.MESTO_PROFILE_TITLE_TEXT

    def test_failed_login(self, driver):
        email_input = driver.find_element(*Locators.MESTO_EMAIL_INPUT)
        email_input.send_keys(Helper.generate_email())

        password_input = driver.find_element(*Locators.MESTO_PASSWORD_INPUT)
        password_input.send_keys(Data.MESTO_PASSWORD)

        enter_button = driver.find_element(*Locators.MESTO_LOGIN_BUTTON)
        enter_button.click()

        WebDriverWait(driver, Data.WAIT_TIME).until(EC.visibility_of_element_located(Locators.MESTO_LOGIN_ERROR_POPUP))

        error_popup = driver.find_element(*Locators.MESTO_LOGIN_ERROR_POPUP)

        assert error_popup.is_displayed()