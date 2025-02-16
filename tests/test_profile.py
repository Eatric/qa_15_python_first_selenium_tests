from data import Data
from locators import Locators


class TestProfile:
    def test_profile(self, loggined_driver):
        profile_title = loggined_driver.find_element(*Locators.MESTO_PROFILE_TITLE)

        assert profile_title.is_displayed() and profile_title.text == Data.MESTO_PROFILE_TITLE_TEXT