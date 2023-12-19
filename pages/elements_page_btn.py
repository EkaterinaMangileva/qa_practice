from locators.elements_page_locators_btn import BtnActions, Scrolling, MouseHover
from pages.base_page import BasePage
from selenium.webdriver import ActionChains
from collections import Counter
from time import sleep


class Button(BasePage):
    locators = BtnActions()

    def double_click2(self):
        self.element_is_visible(BtnActions.BTN_ACTIONS).click()
        self.element_is_visible(BtnActions.DOUBLE_CLICK_BUTTON).click()
        act = ActionChains(self.driver)
        element = self.element_is_visible(BtnActions.CLICK)
        act.double_click(on_element=element).perform()
        text = self.element_is_present(BtnActions.TEXT).text
        assert self.element_is_present(
            BtnActions.TEXT).text == "Congrats, you double clicked!"

    def count_amount_characters(self):
        self.element_is_visible(Scrolling.BTN_ACTIONS).click()
        self.element_is_visible(Scrolling.SCROLLING).click()
        some_text = self.elements_are_present(Scrolling.ALL_TEXT)
        for elements in some_text:
            print(len(elements.text))

    def count_amount_words(self):
        self.element_is_visible(Scrolling.BTN_ACTIONS).click()
        self.element_is_visible(Scrolling.SCROLLING).click()
        some_text = self.elements_are_present(Scrolling.ALL_TEXT)
        for elements in some_text:
            print(len(elements.text.split()))

    def compare_two_texts(self):
        self.element_is_visible(Scrolling.BTN_ACTIONS).click()
        self.element_is_visible(Scrolling.SCROLLING).click()
        first = self.elements_are_present(Scrolling.FIRST_TEXT)
        second = self.elements_are_present(Scrolling.SECOND_TEXT)
        for elements in first:
            len(elements.text.split())
        for some_elements in second:
            len(some_elements.text.split())
        if first == second:
            print("Correct")
        else:
            print("Not correct")

    def count_some_words(self):
        self.element_is_visible(Scrolling.BTN_ACTIONS).click()
        self.element_is_visible(Scrolling.SCROLLING).click()
        some_text = self.elements_are_present(Scrolling.ALL_TEXT)
        for words in some_text:
            print(Counter(words.text.split()))


class Mouse(BasePage):
    locators = MouseHover()

    def show_hidden_text(self):
        self.element_is_visible(MouseHover.BTN_ACTIONS).click()
        self.element_is_visible(MouseHover.MOUSE_HOVER).click()
        act = ActionChains(self.driver)
        button = self.element_is_present(MouseHover.BUTTON)
        act.move_to_element(button).perform()
        text_button = self.elements_are_present(MouseHover.UNDER_BUTTON_TEXT)
        for words in text_button:
            assert words.text == "I am shown when someone hovers over the text above."

    def show_hidden_other_text(self):
        self.element_is_visible(MouseHover.BTN_ACTIONS).click()
        self.element_is_visible(MouseHover.MOUSE_HOVER).click()
        act = ActionChains(self.driver)
        button = self.element_is_present(MouseHover.TEXT)
        act.move_to_element(button).perform()
        text_button = self.elements_are_present(MouseHover.TEXT)
        for words in text_button:
            assert words.text == 'HOVERED'
