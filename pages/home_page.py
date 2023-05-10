from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_result_page import SearchResultPage


class HomePage(BasePage):
    LOGIN_BTN = (By.ID, 'nav-link-accountList')
    SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    HOME_PAGE_BANNER = (By.ID, 'gw-desktop-herotator')

    def click_sign_in(self):
        self.click_element(*self.LOGIN_BTN)

        return LoginPage(self.driver)

    def search_for(self, search_keyword):
        self.send_text(search_keyword, *self.SEARCH_BOX)
        self.click_element(*self.SEARCH_BTN)

        return SearchResultPage(self.driver)

