from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import GooglePageLocators


class GooglePage(BasePage):
    URL = "https://google.com/"

    def __init__(self, driver, url=URL):
        super().__init__(driver, url)

    def search_field(self) -> WebElement:
        return self.is_visible(GooglePageLocators.GOOGLE_SEARCH_FIELD)

    def first_link_on_google_search(self) -> WebElement:
        return self.is_clickable(GooglePageLocators.FIRST_URL_ON_PAGE_GOOGLE)

    def click_enter_google_search(self) -> WebElement:
        return self.click_enter(GooglePageLocators.GOOGLE_SEARCH_FIELD)
