from selenium.webdriver.common.by import By


class FormsLogin:
    FORMS = (By.XPATH, "(//a[@id='forms'])[1]")
    LOGIN = (By.XPATH, "//a[@id='login']")
    COPY = (By.XPATH, "//small[@id='emailHelp']")
    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[@id='submitLoginBtn']")
    TRY_AGAIN = (By.XPATH, "//div[@style='display: block;']")
