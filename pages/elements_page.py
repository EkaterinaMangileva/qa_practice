import time

from locators.elements_page_locators import FormsLogin
from pages.base_page import BasePage
from generator.generator import create_account


class LoginNewAccount(BasePage):
    locators = FormsLogin()

    def make_new_akk(self):
        account = next(create_account())
        new_email = account.email
        new_password = account.password
        self.element_is_visible(FormsLogin.FORMS).click()
        self.element_is_visible(FormsLogin.LOGIN).click()
        self.element_is_visible(FormsLogin.EMAIL).send_keys(new_email)
        self.element_is_visible(FormsLogin.PASSWORD).send_keys(new_password)
        self.element_is_visible(FormsLogin.SUBMIT).click()
        text = self.element_is_present(FormsLogin.TRY_AGAIN).text
        assert self.element_is_present(
            FormsLogin.TRY_AGAIN).text == "Bad credentials! Please try again! Make sure that you've registered."

    def make_new_akk_insert(self):
        self.element_is_visible(FormsLogin.FORMS).click()
        self.element_is_visible(FormsLogin.LOGIN).click()
        self.element_is_visible(FormsLogin.EMAIL).send_keys("admin@admin.com")
        self.element_is_visible(FormsLogin.PASSWORD).send_keys("admin123")
        self.element_is_visible(FormsLogin.SUBMIT).click()

    def make_new_akk_hard(self):
        self.element_is_visible(FormsLogin.FORMS).click()
        self.element_is_visible(FormsLogin.LOGIN).click()
        text_from_email = self.element_is_visible(FormsLogin.COPY).text
        print(text_from_email.split()[3])
        print(text_from_email.split()[5])
        self.element_is_visible(FormsLogin.EMAIL).send_keys(text_from_email.split()[3])
        self.element_is_visible(FormsLogin.PASSWORD).send_keys(text_from_email.split()[5])
        self.element_is_visible(FormsLogin.SUBMIT).click()

