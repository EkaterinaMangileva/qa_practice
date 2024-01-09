from selenium.webdriver.common.by import By


class Tables:
    TABLES = (By.XPATH, "//a[contains(text(), 'Tables')]")
    DYNAMIC_TABLE = (By.XPATH, "//a[contains(text(), 'Dynamic Table')]")
    TABLE = (By.XPATH, "(//tbody[@id='data-tbody']//td)")
    PHOTOS = (By.XPATH, "//img[@src]")
    ONE_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[1])")
    TWO_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[2])")
    THREE_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[3])")
    FOUR_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[4])")
    FIVE_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[5])")
    SIX_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[6])")
    SEVEN_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[7])")
    EIGHT_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[8])")
    NINE_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[9])")
    TEN_STRING = (By.XPATH, "(//tbody[@id='data-tbody']//tr[10])")

