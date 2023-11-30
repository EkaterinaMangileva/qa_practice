from pages.elements_page import LoginNewAccount


class TestNewAccount:
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
