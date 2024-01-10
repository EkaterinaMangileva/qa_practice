from selenium.webdriver.common.by import By


class Loader:
    LOADER_PAGE = (By.XPATH, "//a[@id='loader']")
    LOADER_WAIT = (By.XPATH, "//div[@id='loader']")
    HEADER = (By.XPATH, "//h2[contains(text(), 'Tada!')]")
    SOME_TEXT = (By.XPATH, "//p[contains(text(), 'Some text')]")

