from selenium.webdriver.common.by import By
from locators.elements_page_locators_newtab import NewBrowserTab, NewBrowserWindow
from pages.base_page import BasePage


class NewTab(BasePage):
    locators = NewBrowserTab()

    def check_newtab_table_elements(self):
        self.element_is_visible(NewBrowserTab.NEW_TAB).click()
        self.element_is_visible(NewBrowserTab.NEW_BROWSER_TAB).click()
        self.element_is_visible(NewBrowserTab.PRESS_ME).click()
        self.switch_handles_window()
        table = self.elements_are_present(NewBrowserTab.TABLE)
        for elements in table:
            print(elements.text)

    def check_newtab_table_element(self):
        self.element_is_visible(NewBrowserTab.NEW_TAB).click()
        self.element_is_visible(NewBrowserTab.NEW_BROWSER_TAB).click()
        self.element_is_visible(NewBrowserTab.PRESS_ME).click()
        self.switch_handles_window()
        table = self.elements_are_present(NewBrowserTab.TABLE)
        for element in table:
            if 'Mark' == element.text:
                print("Mark ok")

    def check_newtab_table_all(self):
        self.element_is_visible(NewBrowserTab.NEW_TAB).click()
        self.element_is_visible(NewBrowserTab.NEW_BROWSER_TAB).click()
        self.element_is_visible(NewBrowserTab.PRESS_ME).click()
        self.switch_handles_window()
        table = self.elements_are_present(NewBrowserTab.TABLE)
        elements = [
            "Mark", "Otto", "mo@email.com",
            "Jacob", "Thornton", "jacob_t@yahoo.com",
            "Larry", "Bow", "lbow@gmail.com",
            "Bobby", "Spencer", "bobby_23@gmail.com",
            "Mark", "Icarus", "el_icarus@yahoo.com"
        ]
        found_texts = []
        for element in table:
            found_texts.append(element.text)
        for item in elements:
            assert item in found_texts, f'{item} не найден в таблице'

    def check_newtab_table_first_string(self):
        self.element_is_visible(NewBrowserTab.NEW_TAB).click()
        self.element_is_visible(NewBrowserTab.NEW_BROWSER_TAB).click()
        self.element_is_visible(NewBrowserTab.PRESS_ME).click()
        self.switch_handles_window()
        table = self.elements_are_present(NewBrowserTab.TABLE_FIRST_STR)
        elements = [
            "Mark", "Otto", "Spencer"
        ]
        found_texts = []
        for element in table:
            found_texts.append(element.text)
        for item in elements:
            assert item in found_texts, f'{item} не найден в 1 строке таблицы'


class Window(BasePage):
    locators = NewBrowserWindow

    def check_newwindow_table_element(self):
        self.element_is_visible(NewBrowserWindow.NEW_TAB).click()
        self.element_is_visible(NewBrowserWindow.NEW_BROWSER_WINDOW).click()
        self.element_is_visible(NewBrowserWindow.PRESS_ME).click()
        self.switch_handles_window()
        table = self.elements_are_present(NewBrowserWindow.TABLE)
        for element in table:
            if 'Larry' == element.text:
                print("Larry ok")

    def check_newwindow_table_second_str(self):
        self.element_is_visible(NewBrowserWindow.NEW_TAB).click()
        self.element_is_visible(NewBrowserWindow.NEW_BROWSER_WINDOW).click()
        self.element_is_visible(NewBrowserWindow.PRESS_ME).click()
        self.switch_handles_window()
        table = self.elements_are_present(NewBrowserWindow.TABLE_SECOND_STR)
        elements = [
            "Jacob", "Thor", "jacob_t@yahoo.com"
        ]
        found_texts = []
        for element in table:
            found_texts.append(element.text)
        for item in elements:
            assert item in found_texts, f'{item} не найден в 2 строке таблицы'

    def check_newwindow_table_elements(self):
        self.element_is_visible(NewBrowserWindow.NEW_TAB).click()
        self.element_is_visible(NewBrowserWindow.NEW_BROWSER_WINDOW).click()
        self.element_is_visible(NewBrowserWindow.PRESS_ME).click()
        self.switch_handles_window()
        table = self.elements_are_present(NewBrowserWindow.TABLE)
        for elements in table:
            print(elements.text)


