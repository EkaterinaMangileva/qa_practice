import time

from pages.elements_page_file_upload import UploadSomeFile


class TestUploadSomeFile:
    # Тест, который проверяет, что файл загрузился
    def test_upload_file(self, driver):
        test_account = UploadSomeFile(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check_file = test_account.upload_new_type()

    # Тест, который проверяет, что текст появился даже без загрузки файла (негативный)
    def test_do_not_upload_file(self, driver):
        test_account = UploadSomeFile(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        check_file = test_account.do_not_upload_new_type()