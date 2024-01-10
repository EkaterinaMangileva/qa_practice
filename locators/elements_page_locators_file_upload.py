from selenium.webdriver.common.by import By
from random import randint


class FileUpload:
    FILEUPLOAD = (By.XPATH, "//a[@id='file-upload-item']")
    CHOOSE_FILE = (By.XPATH, "//input[@id='file_upload']")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    TEXT = (By.XPATH, "//div[contains(text(), 'You have successfully')]")