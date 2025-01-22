from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    FIRST_ITEM = (By.CSS_SELECTOR, ".s-item__link")

    def click_first_item(self):
        self.wait_for_element(self.FIRST_ITEM).click()
