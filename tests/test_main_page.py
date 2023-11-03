from pages.google_page import GooglePage
from pages.main_page import MainPage
from data.locators import telegram_contact


class TestOrderPresentationYellowButton:

    def test_telegram_link(self,driver):
        page = GooglePage(driver)
        page.open()
        page.search_field().send_keys('Byndyusoft')
        page.click_enter_google_search()
        page.first_link_on_google_search().click()

        page = MainPage(driver)
        page.order_a_presentation_yellow_button().click()

        assert page.write_us_telegram_contact() == telegram_contact, f'Вместо правильного телеграмма , указан {page.write_us_telegram_contact()}'