from selenium.webdriver.common.by import By


class Locators:
    MESTO_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Email']")
    MESTO_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']") # tuple

    MESTO_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    MESTO_PROFILE_TITLE = (By.CLASS_NAME, "profile__title")

    MESTO_LOGIN_ERROR_POPUP = (By.XPATH, "//div[contains(@class, 'popup_is-opened')]/descendant::p[contains(text(), 'Что-то пошло не так!')]")
