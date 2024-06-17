from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    CITY_POPUP_CLOSE_BTN = (By.XPATH, "//button[contains(text(), 'Да, я здесь')]")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input.header-search__input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.header-search__button")

    def close_city_popup(self):
        try:
            close_button = self.wait_for_element_to_be_clickable(10, *self.CITY_POPUP_CLOSE_BTN)
            close_button.click()
            self.wait_for_element(10, (By.XPATH, "//button[contains(text(), 'Да, я здесь')]"))
        except Exception as e:
            print("Всплывающее окно с выбором города не обнаружено или не удалось закрыть")
            print(str(e))

    def search_for_item(self, query):
        search_input = self.wait_for_element_to_be_clickable(10, *self.SEARCH_INPUT)
        search_input.clear()
        search_input.send_keys(query)
        search_button = self.wait_for_element_to_be_clickable(10, *self.SEARCH_BUTTON)
        search_button.click()
