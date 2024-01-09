from locators.elements_page_locators_buttons import ButtonsLocators
from pages.base_page import BasePage


class ButtonsTest(BasePage):
    locators = ButtonsLocators()

    def random_click(self):
        self.element_is_visible(ButtonsLocators.BUTTONS).click()
        self.element_is_visible(ButtonsLocators.CHECKBOXES).click()
        first_checkbox = self.element_is_visible(ButtonsLocators.CHECK_ME_ONE)
        second_checkbox = self.element_is_visible(ButtonsLocators.CHECK_ME_TWO)
        third_checkbox = self.element_is_visible(ButtonsLocators.CHECK_ME_THREE)
        first_checkbox.click()
        if first_checkbox.is_selected():
            print("Первый чекбокс заполнен")
        else:
            print("Первый чекбокс пустой")
        if second_checkbox.is_selected():
            print("Второй чекбокс заполнен")
        else:
            print("Второй чекбокс пустой")
        third_checkbox.click()
        if third_checkbox.is_selected():
            print("Третий чекбокс заполнен")
        else:
            print("Третий чекбокс пустой")
        self.element_is_visible(ButtonsLocators.RESET).click()
