from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def wait_for_element(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))
