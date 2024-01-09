from selenium.webdriver.common.by import By
from random import randint


class DatePicker:
    DATE_PICKER = (By.XPATH, "//a[@id='date-picker']")
    RANGE_DATE_PICKER = (By.XPATH, "//input[@id='range-date-calendar']")
    RANGE_FIRST_DAY = (By.XPATH, f"(//tbody/tr/td)[{randint(0, 40)}]")
    RANGE_SECOND_DAY = (By.XPATH, f"(//tbody/tr/td)[{randint(0, 83)}]")
    APPLY_BUTTON = (By.XPATH, "//button[contains(text(),'Apply')]")
    BASIC_DATE_PICKER = (By.XPATH, "//input[@id='calendar']")
    BASIC_DATE_JANUARY = (By.XPATH, "//th[contains(text(), 'January')]")
    BASIC_DATE_YEARS = (By.XPATH, "(//th[contains(text(), '2024')])[2]")
    BASIC_THIS_DECADE = (By.XPATH, f"(//span[@class='year'])[{randint(0, 9)}]")
    BASIC_MONTH = (By.XPATH, f"(//span[@class='month'])[{randint(0, 11)}]")
    BASIC_DAY = (By.XPATH, f"(//td[@class='day'])[{randint(0, 30)}]")
