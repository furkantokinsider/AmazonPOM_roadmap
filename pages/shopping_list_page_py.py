from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShoppingListPage(BasePage):
    PRODUCT_NAME_IN_LIST = (By.XPATH, '//h2/a[@class="a-link-normal"]')
    DELETE_BTN = (By.CSS_SELECTOR, 'span[data-action="reg-item-delete"]')
    DELETE_CONFIRMATION_BTN = (By.CLASS_NAME, 'a-alert-inline-success')

    def remove_item_from_shopping_list(self):
        self.click_element(*self.DELETE_BTN)

    def get_product_name_in_list(self):
        product_name = self.find_element(*self.PRODUCT_NAME_IN_LIST).text

        return product_name

    def is_delete_confirmation_displayed(self):
        return self.DELETE_CONFIRMATION_BTN
