import time

from pages.elements_page_newtab import NewTab, Window


class TestNewTab:
    # Тест, который выводит все значения из таблички
    def test_newtab_check_all_elements(self, driver):
        test_account = NewTab(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check = test_account.check_newtab_table_elements()

    # Тест, который проверяет, есть ли значение "Mark" в табличке
    def test_newtab_table_check(self, driver):
        test_account = NewTab(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check = test_account.check_newtab_table_element()

    # Тест, который проверяет, есть ли в табличке все перечисленные значения
    def test_newtab_table_check_elements(self, driver):
        test_account = NewTab(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check = test_account.check_newtab_table_all()

    # Тест, который проверяет, есть ли в первой строке таблички перечисленные значения (нет)
    def test_newtab_table_first_str(self, driver):
        test_account = NewTab(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check = test_account.check_newtab_table_first_string()


class TestBrowserWindow:
    # Тест, который проверяет, есть ли значение "Larry" в табличке
    def test_newwindow_table_check(self, driver):
        test_account = Window(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check = test_account.check_newwindow_table_element()

    # Тест, который проверяет, есть ли во второй строчке таблички перечисленные значения (нет)
    def test_newwindow_table_check_second_atr(self, driver):
        test_account = Window(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check = test_account.check_newwindow_table_second_str()

    # Тест, который выводит все значения из таблички
    def test_newwindow_table_all_elements(self, driver):
        test_account = Window(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check = test_account.check_newwindow_table_elements()


