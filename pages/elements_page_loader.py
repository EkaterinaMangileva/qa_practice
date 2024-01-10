from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from locators.elements_page_locators_loader import Loader
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class WaitLoader(BasePage):
    locators = Loader()

    def wait_loader_for_text(self):
        self.element_is_visible(Loader.LOADER_PAGE).click()
        try:
            # header = EC.presence_of_element_located(self.element_is_visible(Loader.HEADER))
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Loader.HEADER))
            print("Page is ready")
        except TimeoutException:
            print("Loading took too much time")
        assert self.element_is_present(
            Loader.SOME_TEXT).text == "Some text in my newly loaded page.."
