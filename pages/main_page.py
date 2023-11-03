from selenium.webdriver.remote.webelement import WebElement
from base.base_page import BasePage
from data.locators import MainPageLocators


class MainPage(BasePage):


    URL = "https://byndyusoft.com/"

    def __init__(self, driver , url=URL):
        super().__init__(driver, url)

    def order_a_presentation_yellow_button(self) -> WebElement:
        self.go_to_element(MainPageLocators.YELLOW_BUTTON_ORDER_PRESENTATION)
        return self.is_clickable(MainPageLocators.YELLOW_BUTTON_ORDER_PRESENTATION)

    def write_us_telegram_contact(self):
        return self.get_attribute(MainPageLocators.TELEGRAM_CONTACT_BUTTON,'href')


