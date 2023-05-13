from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_TEXT = (By.TAG_NAME, 'h1')
    EMAIL_TEXTBOX = (By.ID, 'ap_email')
    CONTINUE_BTN = (By.ID, 'continue')
    PASSWORD_TEXTBOX = (By.ID, 'ap_password')
    SIGN_IN_BTN = (By.ID, 'signInSubmit')

    def fill_email_textbox(self, email):
        self.send_text(email, *self.EMAIL_TEXTBOX)

    def click_continue(self):
        self.click_element(*self.CONTINUE_BTN)

    def fill_password_textbox(self, password):
        self.send_text(password, *self.PASSWORD_TEXTBOX)

    def click_sign_in(self):
        self.click_element(*self.SIGN_IN_BTN)

    def is_login_text_visible(self):
        return self.LOGIN_TEXT

    def wait_for_password_textbox(self):
        self.wait_element(*self.PASSWORD_TEXTBOX)