from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.shopping_list_page_py import ShoppingListPage


class ProductPage(BasePage):
    ADD_TO_LIST_BTN = (By.ID, 'add-to-wishlist-button-submit')
    SHOPPING_LIST_BTN = (By.ID, 'huc-list-link')
    PRODUCT_NAME = (By.ID, 'productTitle')

    def add_to_shopping_list(self):
        self.wait_element(*self.ADD_TO_LIST_BTN).click()

    def go_to_shopping_list_page(self):
        self.click_element(*self.SHOPPING_LIST_BTN)

        return ShoppingListPage(self.driver)

    def get_product_name(self):
        product_name = self.find_element(*self.PRODUCT_NAME).text

        return product_name
