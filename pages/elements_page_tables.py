import time
import urllib
import requests

from locators.elements_page_locators_tables import Tables
from pages.base_page import BasePage


class CheckTables(BasePage):
    locators = Tables()

    def import_info_from_table(self):
        self.element_is_visible(Tables.TABLES).click()
        self.element_is_visible(Tables.DYNAMIC_TABLE).click()
        table = self.elements_are_present(Tables.TABLE)
        for elements in table:
            print(elements.text)

    def download_avatars(self):
        self.element_is_visible(Tables.TABLES).click()
        self.element_is_visible(Tables.DYNAMIC_TABLE).click()
        imgResults = self.elements_are_present(Tables.PHOTOS)
        src = []
        for img in imgResults:
            src.append(img.get_attribute('src'))
        # print(src)
        for i in range(10): urllib.request.urlretrieve(str(src[i]), "avatars/photo{}.jpg".format(i))

    def import_text_from_table(self):
        self.element_is_visible(Tables.TABLES).click()
        self.element_is_visible(Tables.DYNAMIC_TABLE).click()
        one = self.element_is_present(Tables.ONE_STRING)
        two = self.element_is_present(Tables.TWO_STRING)
        three = self.element_is_present(Tables.THREE_STRING)
        four = self.element_is_present(Tables.FOUR_STRING)
        five = self.element_is_present(Tables.FIVE_STRING)
        six = self.element_is_present(Tables.SIX_STRING)
        seven = self.element_is_present(Tables.SEVEN_STRING)
        eight = self.element_is_present(Tables.EIGHT_STRING)
        nine = self.element_is_present(Tables.NINE_STRING)
        ten = self.element_is_present(Tables.TEN_STRING)
        for elements in one, two, three, four, five, six, seven, eight, nine, ten:
            print(elements.text.split())

    def check_text_in_table(self):
        self.element_is_visible(Tables.TABLES).click()
        self.element_is_visible(Tables.DYNAMIC_TABLE).click()
        table = [
            Tables.ONE_STRING,
            Tables.TWO_STRING,
            Tables.THREE_STRING,
            Tables.FOUR_STRING,
            Tables.FIVE_STRING,
            Tables.SIX_STRING,
            Tables.SEVEN_STRING,
            Tables.EIGHT_STRING,
            Tables.NINE_STRING,
            Tables.TEN_STRING
        ]
        for check_it in table:
            assert self.element_is_visible(check_it), f'Элемент {check_it} не отображен'