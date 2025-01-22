from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ItemPage(BasePage):
    ADD_TO_CART_BUTTON = (By.ID, "atcRedesignId_btn")
    CART_COUNT = (By.CSS_SELECTOR, "#gh-cart-n")

    def add_to_cart(self):
        self.wait_for_element(self.ADD_TO_CART_BUTTON).click()

    def get_cart_count(self):
        return int(self.wait_for_element(self.CART_COUNT).text)
