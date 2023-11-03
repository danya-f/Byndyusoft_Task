import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


@pytest.fixture()
def options():
    options = Options()
    # options.add_argument('--headless')
    options.add_argument('--start-maximized')
    return options

@pytest.fixture()
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
