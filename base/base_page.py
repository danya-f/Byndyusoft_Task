from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def is_visible(self, locator) -> WebElement:
        return wait(self.driver, timeout=20).until(EC.visibility_of_element_located(locator))

    def is_clickable(self, locator) -> WebElement:
        return wait(self.driver, timeout=20).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, locator):
        actions = ActionChains(self.driver)
        return actions.move_to_element(self.driver.find_element(*locator)).perform()

    def current_url(self):
        return self.driver.current_url

    def click_enter(self, locator):
        return wait(self.driver, timeout=20).until(EC.element_to_be_clickable(locator)).send_keys(Keys.ENTER)

    def get_attribute(self, locator, attribute):
        return wait(self.driver, timeout=20).until(EC.visibility_of_element_located(locator)).get_attribute(attribute)
