from locators.elements_page_locators_date_picker import DatePicker
from pages.base_page import BasePage


class CalendarPicker(BasePage):
    locators = DatePicker()

    def choose_range_date_picker_example(self):
        self.element_is_visible(DatePicker.DATE_PICKER).click()
        self.element_is_visible(DatePicker.RANGE_DATE_PICKER).click()
        self.element_is_visible(DatePicker.RANGE_FIRST_DAY).click()
        self.element_is_visible(DatePicker.RANGE_SECOND_DAY).click()
        self.element_is_visible(DatePicker.APPLY_BUTTON).click()

    def choose_basic_date_picker_example(self):
        self.element_is_visible(DatePicker.DATE_PICKER).click()
        self.element_is_visible(DatePicker.BASIC_DATE_PICKER).click()
        self.element_is_visible(DatePicker.BASIC_DATE_JANUARY).click()
        self.element_is_visible(DatePicker.BASIC_DATE_YEARS).click()
        self.element_is_visible(DatePicker.BASIC_THIS_DECADE).click()
        self.element_is_visible(DatePicker.BASIC_MONTH).click()
        self.element_is_visible(DatePicker.BASIC_DAY).click()
