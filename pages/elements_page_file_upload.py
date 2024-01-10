import time

from locators.elements_page_locators_file_upload import FileUpload
from pages.base_page import BasePage


class UploadSomeFile(BasePage):
    locators = FileUpload()

    def upload_new_type(self):
        self.element_is_visible(FileUpload.FILEUPLOAD).click()
        self.element_is_visible(FileUpload.CHOOSE_FILE).send_keys(r"C:\Users\Katerina\Desktop\cat.jpg")
        self.element_is_visible(FileUpload.SUBMIT).click()
        some_text = self.element_is_present(FileUpload.TEXT)
        some_doc = "cat.jpg"
        assert some_text.text == "You have successfully uploaded \"cat.jpg\""

    def do_not_upload_new_type(self):
        self.element_is_visible(FileUpload.FILEUPLOAD).click()
        self.element_is_visible(FileUpload.SUBMIT).click()
        some_text = self.element_is_present(FileUpload.TEXT)
        assert some_text.text == "You have successfully uploaded \"\""
