from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    URL = "https://www.ebay.com"
    SEARCH_BOX = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")

    def open(self):
        self.browser.get(self.URL)

    def search_for_item(self, item):
        self.wait_for_element(self.SEARCH_BOX).send_keys(item)
        self.wait_for_element(self.SEARCH_BUTTON).click()
