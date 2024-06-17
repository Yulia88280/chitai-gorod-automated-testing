import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from config.environment import UI_BASE_URL
from config.test_data import TEST_SEARCH_QUERY

class BaseTest:
    @pytest.fixture(scope="class")
    def driver(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

@allure.feature('Поиск товаров')
class TestSearch(BaseTest):

    @allure.story('Наличие поля поиска')
    @allure.step("Проверка наличия поля поиска")
    def test_search_box_presence(self, driver):
        home_page = HomePage(driver)
        driver.get(UI_BASE_URL)
        home_page.close_city_popup()
        search_box = home_page.find_element(*HomePage.SEARCH_INPUT)
        assert search_box.is_displayed(), "Поле поиска не отображается"

    @allure.story('Автодополнение в поиске')
    @allure.step("Проверка автодополнения в поиске")
    def test_search_autocomplete(self, driver):
        home_page = HomePage(driver)
        driver.get(UI_BASE_URL)
        home_page.close_city_popup()
        search_box = home_page.find_element(*HomePage.SEARCH_INPUT)
        search_box.send_keys("Гарри")
        suggestions = home_page.wait_for_element(10, By.CLASS_NAME, "result-item--suggests-type")
        assert len(suggestions) > 0, "Автодополнение не работает"

    @allure.story('Наличие кнопки поиска')
    @allure.step("Проверка кнопки поиска")
    def test_search_button(self, driver):
        home_page = HomePage(driver)
        driver.get(UI_BASE_URL)
        home_page.close_city_popup()
        search_button = home_page.find_element(*HomePage.SEARCH_BUTTON)
        assert search_button.is_displayed(), "Кнопка поиска не отображается"
        assert search_button.is_enabled(), "Кнопка поиска неактивна"

    @allure.story('Фильтрация результатов поиска')
    @allure.step("Проверка фильтрации результатов поиска")
    def test_search_filter(self, driver):
        home_page = HomePage(driver)
        search_results_page = SearchResultsPage(driver)
        driver.get(UI_BASE_URL)
        home_page.close_city_popup()
        home_page.search_for_item(TEST_SEARCH_QUERY)
        search_results_page.click_filter_available()
        filter_options = search_results_page.get_sort_options()
        assert len(filter_options) > 0, "Опции фильтрации не отображаются"

    @allure.story('Сортировка результатов поиска')
    @allure.step("Проверка сортировки результатов поиска")
    def test_search_sort(self, driver):
        home_page = HomePage(driver)
        search_results_page = SearchResultsPage(driver)
        driver.get(UI_BASE_URL)
        home_page.close_city_popup()
        home_page.search_for_item(TEST_SEARCH_QUERY)
        search_results_page.click_sort_button()
        sort_options = search_results_page.get_sort_options()
        assert len(sort_options) > 0, "Опции сортировки не отображаются"

    @allure.story('Проверка наличия товаров в результатах поиска')
    @allure.step("Проверка наличия товаров в результатах поиска")
    def test_search_results(self, driver):
        home_page = HomePage(driver)
        search_results_page = SearchResultsPage(driver)
        driver.get(UI_BASE_URL)
        home_page.close_city_popup()
        home_page.search_for_item(TEST_SEARCH_QUERY)
        results_message = search_results_page.get_results_message()
        assert results_message.is_displayed(), "Сообщение о количестве найденных результатов не отображается"
        products_list = search_results_page.get_products_list()
        assert products_list.is_displayed(), "Список продуктов не отображается"
