from selenium.webdriver.common.by import By
from random import randint


class BtnActions:
    BTN_ACTIONS = (By.XPATH, "//a[@id='actions']")
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//a[@id='double-click']")
    CLICK = (By.XPATH, "//button[@id='double-click-btn']")
    TEXT = (By.XPATH, "(//div[(text()='Congrats, you double clicked!')])")


class Scrolling:
    BTN_ACTIONS = (By.XPATH, "//a[@id='actions']")
    SCROLLING = (By.XPATH, "//a[@id='scrolling']")
    FIRST_TEXT = (By.XPATH, "//p[contains(text(), 'Scirem')]")
    SECOND_TEXT = (By.XPATH, "//div[contains(text(), 'Lorem')]")
    ALL_TEXT = (By.XPATH, "//div[@id='main']")


class MouseHover:
    BTN_ACTIONS = (By.XPATH, "//a[@id='actions']")
    MOUSE_HOVER = (By.XPATH, "//a[@id='mouse-hover']")
    TEXT = (By.XPATH, "//p[@id='demo']")
    BUTTON = (By.XPATH, "//button[@id='button-hover-over']")
    UNDER_BUTTON_TEXT = (By.XPATH, "//div[@class='hide']")


class HideElement:
    BTN_ACTIONS = (By.XPATH, "//a[@id='actions']")
    HIDE_ELEMENT = (By.XPATH, "//a[@id='show-hide-elements']")
    BUTTON = (By.XPATH, "//button[@id='showHideBtn']")
    HIDDEN_TEXT = (By.XPATH, "//DIV[@id='hiddenText']")
