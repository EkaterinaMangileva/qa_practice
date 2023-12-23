import time

from pages.elements_page_forms import LoginNewAccount


class TestFormsLogin:
    def test_create_new_account(self, driver):
        test_account = LoginNewAccount(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.make_new_akk()

    def test_create_new_account_insert(self, driver):
        test_account = LoginNewAccount(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        insert = test_account.make_new_akk_insert()
        current_page_url = driver.current_url
        print("The URL of the current page is: " + current_page_url)

    def test_create_new_account_hard_level(self, driver):
        test_account = LoginNewAccount(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        hard = test_account.make_new_akk_hard()
        get_url = driver.current_url
        assert "auth_ecommerce" in get_url

    # Тест, который валится (на проверку)
    def test_check_all_elements(self, driver):
        test_account = LoginNewAccount(driver, "https://qa-practice.netlify.app/auth_ecommerce")
        test_account.open()
        check_all_elements = test_account.check_all_elements_on_page()


# Тест, который заполнит форму на русском языке
class TestRegister:
    def test_register_fill(self, driver):
        test_account = LoginNewAccount(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        fill_all_forms = test_account.fill_form_register()


# Тест, который заполняет форму на английском языке
class TestRegisterFr:
    def test_register_fill_fr(self, driver):
        test_account = LoginNewAccount(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        fill_all_forms= test_account.fill_form_register_fr()


class TestRecoverPassword:
    def test_recover_password(self, driver):
        test_account = LoginNewAccount(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        fill_form = test_account.filled_register_password()


