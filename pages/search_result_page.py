from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class SearchResultPage(BasePage):
    RESULT_PAGE_LEFT_BANNER = (By.ID, 's-refinements')
    SEARCH_RESULT_FOR = (By.CSS_SELECTOR, "span[class='a-color-state a-text-bold']")
    SECOND_PAGE_BTN = (By.CSS_SELECTOR, 'a[aria-label = "Go to page 2"]')
    CURRENT_PAGE = (By.CLASS_NAME, 's-pagination-selected')
    THIRD_PRODUCT = (By.XPATH, "//div[@data-index='4']//h2/a")

    def click_second_page(self):
        self.click_element(*self.SECOND_PAGE_BTN)

    def click_third_product(self):
        self.wait_element(*self.THIRD_PRODUCT).click()

        return ProductPage(self.driver)

    def get_search_result_text(self):
        search_text = self.find_element(*self.SEARCH_RESULT_FOR).text.strip('"')

        return search_text

    def get_current_page(self):
        current_page = self.find_element(*self.CURRENT_PAGE).text

        return current_page

    def is_left_banner_displayed(self):
        return self.find_element(*self.RESULT_PAGE_LEFT_BANNER)

    def wait_for_second_page_button(self):
        self.wait_element(*self.SECOND_PAGE_BTN)
