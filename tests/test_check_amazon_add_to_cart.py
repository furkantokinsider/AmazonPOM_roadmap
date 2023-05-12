from tests.base_test import BaseTest
from pages.home_page import HomePage


class TestCheckAmazonAddToCart(BaseTest):
    email = 'furkantok3.14@gmail.com'
    password = 'CpST2fScZmn#y3/'
    search_keyword = 'samsung'
    page_count = '2'

    def test_check_amazon_add_to_cart(self):
        home_page = HomePage(self.driver)
        home_page.wait_element(*home_page.SEARCH_BOX)
        self.assertTrue(*home_page.HOME_PAGE_BANNER)
        login_page = home_page.click_sign_in()

        self.assertTrue(*login_page.LOGIN_TEXT)
        login_page.fill_email_textbox(self.email)
        login_page.click_continue()
        login_page.wait_element(*login_page.PASSWORD_TEXTBOX)
        login_page.fill_password_textbox(self.password)
        login_page.click_sign_in()

        self.assertTrue(*home_page.HOME_PAGE_BANNER)
        search_result_page = home_page.search_for(self.search_keyword)
        self.assertEquals(search_result_page.get_search_result_text(), self.search_keyword)
        self.assertTrue(*search_result_page.RESULT_PAGE_LEFT_BANNER)
        search_result_page.wait_element(*search_result_page.SECOND_PAGE_BTN)
        search_result_page.click_second_page()
        self.assertEquals(*search_result_page.get_current_page(), self.page_count)

        product_page = search_result_page.click_third_product()
        product_page.wait_element(*product_page.ADD_TO_LIST_BTN)
        self.assertTrue(*product_page.ADD_TO_LIST_BTN)
        product_page.add_to_shopping_list()
        product_page.wait_element(*product_page.SHOPPING_LIST_BTN)
        product_name_in_product_page = product_page.get_product_name()

        shopping_list_page = product_page.go_to_shopping_list_page()
        self.assertEquals(product_name_in_product_page, shopping_list_page.get_product_name_in_list())
        shopping_list_page.remove_item_from_shopping_list()
        self.assertTrue(*shopping_list_page.DELETE_CONFIRMATION_BTN)

    def tearDown(self):
        self.driver.quit()
