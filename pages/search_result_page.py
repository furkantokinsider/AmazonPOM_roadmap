from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchResultPage(BasePage):
    RESULT_PAGE_LEFT_BANNER = (By.ID, 's-refinements')
    SEARCH_RESULT_FOR = (By.CSS_SELECTOR, "span[class='a-color-state a-text-bold']")
    SECOND_PAGE_BTN = (By.CSS_SELECTOR, 'a[aria-label = "Go to page 2"]')
    CURRENT_PAGE = (By.CSS_SELECTOR, '.s-pagination-selected')
    THIRD_PRODUCT = (By.XPATH, "//div[@data-index='4']//h2/a")

    def click_second_page(self):
        self.click_element(*self.SECOND_PAGE_BTN)

    def click_third_product(self):
        self.wait_element(*self.THIRD_PRODUCT).click()

        return ProductPage(self.driver)

    def get_search_result_text(self):
        search_text = self.find_element(*SearchResultPage.SEARCH_RESULT_FOR).text.strip('"')

        return search_text

    def get_current_page(self):
        current_page = self.find_element(*SearchResultPage.CURRENT_PAGE).text

        return current_page




