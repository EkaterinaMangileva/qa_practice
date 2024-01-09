import time

from pages.elements_page_tables import CheckTables


class TestTables:
    # Тест, который присылает всю информацию из таблички
    def test_import_info_from_table(self, driver):
        test_account = CheckTables(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        table_text = test_account.import_info_from_table()

    # Тест, который присылает изображения аватарок
    def test_download_avatars(self, driver):
        test_account = CheckTables(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        table_text = test_account.download_avatars()

    # Тест, который построчно присылает информацию из таблицы
    def test_import_text(self, driver):
        test_account = CheckTables(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        table_text = test_account.import_text_from_table()

    # Тест, который проверяет есть ли в таблице текст
    def test_check_text_in_table(self, driver):
        test_account = CheckTables(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        table_text = test_account.check_text_in_table()