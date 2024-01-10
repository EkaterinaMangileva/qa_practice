from pages.elements_page_loader import WaitLoader


class TestLoaderWait:
    # Тест, ждет загрузки
    def test_loader_wait_the_text(self, driver):
        test_account = WaitLoader(driver, "https://qa-practice.netlify.app/")
        test_account.open()
        wait = test_account.wait_loader_for_text()