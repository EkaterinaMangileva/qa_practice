import time

from pages.elements_page_btn import Button, Mouse


class TestButton:
    # Тест, который дважды нажимает на кнопку
    def test_button_double_click(self, driver):
        test_account = Button(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.double_click2()

    # Тест, который считает количество знаков (с пробелами) на странице
    def test_count_amount_characters(self, driver):
        test_account = Button(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.count_amount_characters()

    # Тест, который считает количество слов на странице
    def test_count_amount_words(self, driver):
        test_account = Button(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.count_amount_words()

    # Тест, который проверяет равен ли первый тест - второму
    def test_compare_two_texts(self, driver):
        test_account = Button(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.compare_two_texts()

    # Тест, который считает количество повторений слов в тексте на странице
    def test_count_some_words(self, driver):
        test_account = Button(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.count_some_words()

    # Тест, который проверяет, появился ли скрытый текст при наведении на кнопку
    def test_show_hidden_text(self, driver):
        test_account = Mouse(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.show_hidden_text()

    # Тест, который проверяет, появился ли скрытый текст при наведении на текст
    def test_show_other_hidden_text(self, driver):
        test_account = Mouse(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.show_hidden_other_text()
ё