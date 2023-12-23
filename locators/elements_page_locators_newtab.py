from selenium.webdriver.common.by import By


class NewBrowserTab:
    NEW_TAB = (By.XPATH, '//a[@href="#browserSubmenu"]')
    NEW_BROWSER_TAB = (By.XPATH, '//a[@id="browser-tab"]')
    PRESS_ME = (By.XPATH, "//button[@id='newTabBtn']")
    TABLE = (By.XPATH, "//tbody[text()]//td")
    TABLE_FIRST_STR = (By.XPATH, "(//*[@id='peopleTable']/tbody/tr[1]/td)")


class NewBrowserWindow:
    NEW_TAB = (By.XPATH, '//a[@href="#browserSubmenu"]')
    NEW_BROWSER_WINDOW = (By.XPATH, "//a[@id='browser-window']")
    PRESS_ME = (By.XPATH, "//button[@id='newWindowBtn']")
    TABLE = (By.XPATH, "//tbody[text()]//td")
    TABLE_SECOND_STR = (By.XPATH, "(//*[@id='peopleTable']/tbody/tr[2]/td)")



