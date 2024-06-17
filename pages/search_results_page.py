from .base_page import BasePage
from selenium.webdriver.common.by import By

class SearchResultsPage(BasePage):
    RESULTS_MESSAGE = (By.CLASS_NAME, "search-page__found-message")
    PRODUCTS_LIST = (By.CLASS_NAME, "products-list")
    FILTER_AVAILABLE = (By.XPATH, "//span[@data-chg-facet='onlyAvailable']")
    SORT_BUTTON = (By.CLASS_NAME, "minimal-sort__button")
    SORT_OPTIONS = (By.CLASS_NAME, "minimal-sort__label")

    def get_results_message(self):
        return self.wait_for_element(20, *self.RESULTS_MESSAGE)

    def get_products_list(self):
        return self.wait_for_element(20, *self.PRODUCTS_LIST)

    def click_filter_available(self):
        filter_available = self.wait_for_element(15, *self.FILTER_AVAILABLE)
        filter_available.click()

    def click_sort_button(self):
        sort_button = self.wait_for_element(15, *self.SORT_BUTTON)
        sort_button.click()

    def get_sort_options(self):
        return self.find_elements(*self.SORT_OPTIONS)
