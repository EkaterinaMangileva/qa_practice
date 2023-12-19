import time

from locators.elements_page_locators_forms import FormsLogin, CheckButtonsLogin, FormsRegister, RecoverPassword
from pages.base_page import BasePage
from generator.generator import create_account, register_account, register_account_fr


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

    def check_all_elements_on_page(self):
        check_elements_on_page = [
            CheckButtonsLogin.MAIN_TITLE,
            CheckButtonsLogin.PAGE_TITLE,
            CheckButtonsLogin.EMAIL_TITLE,
            CheckButtonsLogin.EMAIL_BOX,
            CheckButtonsLogin.PASSWORD_TITLE,
            CheckButtonsLogin.PASSWORD_BOX,
            CheckButtonsLogin.BUTTON_SUBMIT,
            CheckButtonsLogin.BUTTON_HOME,
            CheckButtonsLogin.BUTTON_CONTACT,
            CheckButtonsLogin.CROSS,
            CheckButtonsLogin.WELCOME
        ]
        for check_it in check_elements_on_page:
            assert self.element_is_visible(check_it), f'Элемент {check_it} не отображен'

    def fill_form_register(self):
        akk = next(register_account())
        first_name = akk.first_name
        last_name = akk.last_name
        phone_number = akk.phone_number
        email = akk.email
        password = akk.password
        self.element_is_visible(FormsRegister.FORMS).click()
        self.element_is_visible(FormsRegister.REGISTER_B).click()
        self.element_is_visible(FormsRegister.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(FormsRegister.LAST_NAME).send_keys(last_name)
        self.element_is_visible(FormsRegister.PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(FormsRegister.COUNTRY).click()
        self.element_is_visible(FormsRegister.CHOOSE_COUNTRY).click()
        self.element_is_visible(FormsRegister.EMAIL).send_keys(email)
        self.element_is_visible(FormsRegister.PASSWORD).send_keys(password)
        self.element_is_visible(FormsRegister.AGREE).click()
        self.element_is_visible(FormsRegister.REGISTER).click()
        text = self.element_is_visible(FormsRegister.TEXT).text
        assert text == "The account has been successfully created!"

    def fill_form_register_fr(self):
        akk = next(register_account_fr())
        first_name = akk.first_name
        last_name = akk.last_name
        phone_number = akk.phone_number
        email = akk.email
        password = akk.password
        self.element_is_visible(FormsRegister.FORMS).click()
        self.element_is_visible(FormsRegister.REGISTER_B).click()
        self.element_is_visible(FormsRegister.FIRST_NAME).send_keys(first_name)
        self.element_is_visible(FormsRegister.LAST_NAME).send_keys(last_name)
        self.element_is_visible(FormsRegister.PHONE_NUMBER).send_keys(phone_number)
        self.element_is_visible(FormsRegister.COUNTRY).click()
        self.element_is_visible(FormsRegister.CHOOSE_COUNTRY).click()
        self.element_is_visible(FormsRegister.EMAIL).send_keys(email)
        self.element_is_visible(FormsRegister.PASSWORD).send_keys(password)
        self.element_is_visible(FormsRegister.AGREE).click()
        self.element_is_visible(FormsRegister.REGISTER).click()
        text = self.element_is_visible(FormsRegister.TEXT).text
        assert text == "The account has been successfully created!"

    def filled_register_password(self):
        akk = next(register_account())
        email = akk.email
        self.element_is_visible(RecoverPassword.FORMS).click()
        self.element_is_visible(RecoverPassword.RECOVER_PASSWORD).click()
        self.element_is_visible(RecoverPassword.EMAIL).send_keys(email)
        self.element_is_visible(RecoverPassword.BUTTON).click()

