from selenium.webdriver.common.by import By
from random import randint


class FormsLogin:
    FORMS = (By.XPATH, "(//a[@id='forms'])[1]")
    LOGIN = (By.XPATH, "//a[@id='login']")
    COPY = (By.XPATH, "//small[@id='emailHelp']")
    EMAIL = (By.XPATH, "//input[@type='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    SUBMIT = (By.XPATH, "//button[@id='submitLoginBtn']")
    TRY_AGAIN = (By.XPATH, "//div[@style='display: block;']")


class CheckButtonsLogin:
    MAIN_TITLE = (By.XPATH, '//a[text()="QA Practice"]')
    PAGE_TITLE = (By.XPATH, '//div[@id="loginSection"]')
    EMAIL_TITLE = (By.XPATH, '//label[contains(text(), "Email")]')
    EMAIL_BOX = (By.XPATH, '//input[@type="email"]')
    PASSWORD_TITLE = (By.XPATH, '//label[contains(text(), "Password")]')
    PASSWORD_BOX = (By.XPATH, '//input[@type="password"]')
    BUTTON_SUBMIT = (By.XPATH, '//button[@id="submitLoginBtn"]')
    BUTTON_HOME = (By.XPATH, '//a[contains(text(), "Home")]')
    BUTTON_CONTACT = (By.XPATH, '//a[contains(text(), "Contact")]')
    CROSS = (By.XPATH, '//button[@class="navbar-btn"]')
    WELCOME = (By.XPATH, '//h1[@class="display-4"]')


class FormsRegister:
    FORMS = (By.XPATH, "//a[contains(text(), 'Forms')]")
    REGISTER_B = (By.XPATH, "//a[@id='register']")
    FIRST_NAME = (By.XPATH, "//input[@id='firstName']")
    LAST_NAME = (By.XPATH, "//input[@id='lastName']")
    PHONE_NUMBER = (By.XPATH, "//input[@id='phone']")
    COUNTRY = (By.XPATH, "//select[@id='countries_dropdown_menu']")
    CHOOSE_COUNTRY = (By.XPATH, f"(//option[@value])[{randint(0, 245)}]")
    EMAIL = (By.XPATH, "//input[@id='emailAddress']")
    PASSWORD = (By.XPATH, "//input[@id='password']")
    AGREE = (By.XPATH, "//input[@type='checkbox']")
    REGISTER = (By.XPATH, "//button[@id='registerBtn']")
    TEXT = (By.XPATH, "//div[@class='alert alert-danger']")

