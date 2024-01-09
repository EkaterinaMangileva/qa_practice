import time

from pages.elements_page_buttons import ButtonsTest


class TestButtons:
    # Тест, который проверяет какие чекбоксы заполнены
    def test_import_info_from_table(self, driver):
        test_account = ButtonsTest(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        table_text = test_account.random_click()