import time

from pages.elements_page_date_picker import CalendarPicker


# Тест, который выберет дату в первом календаре
class TestRangeDatePicker:
    def test_choose_range_date_picker(self, driver):
        test_account = CalendarPicker(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        create = test_account.choose_range_date_picker_example()

    # Тест, который выберет дату во втором календаре
    class TestBasicDatePicker:
        def test_choose_range_date_picker(self, driver):
            test_account = CalendarPicker(driver, "https://qa-practice.netlify.app/")
            test_account.open()
            create = test_account.choose_basic_date_picker_example()