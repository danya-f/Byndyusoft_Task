from selenium.webdriver.common.by import By

telegram_contact = "http://t.me/alexanderbyndyu"


class GooglePageLocators:
    GOOGLE_SEARCH_FIELD = (By.XPATH, "//*[@class='gLFyf']")
    GOOGLE_ENTER_SEARCH = (By.XPATH, "//*[@class='CcAdNb']")

    FIRST_URL_ON_PAGE_GOOGLE = (By.XPATH, "(//h3[@class='LC20lb MBeuO DKV0Md'])[1]")


class MainPageLocators:
    YELLOW_BUTTON_ORDER_PRESENTATION = (
        By.XPATH, "//section[@class='knowMore']//*[@class='btn btn--lg btn--info js-popup-callback-show']")
    TELEGRAM_CONTACT_BUTTON = (
        By.XPATH, "//*[@class = 'popup-callback__contacts-tg']")
