from selenium.webdriver.common.by import By


class ButtonsLocators:
    BUTTONS = (By.XPATH, "//a[contains(text(), 'Buttons')]")
    CHECKBOXES = (By.XPATH, "//a[@id='checkboxes']")
    CHECK_ME_ONE = (By.XPATH, "//input[@id='checkbox1']")
    CHECK_ME_TWO = (By.XPATH, "//input[@id='checkbox2']")
    CHECK_ME_THREE = (By.XPATH, "//input[@id='checkbox3']")
    RESET = (By.XPATH, "//button[@type='reset']")
    CHECKBOXES_ALL = (By.XPATH, "//input[@class='form-check-input']")