import pytest
import requests
import allure
from config.environment import API_BASE_URL, TOKEN
from config.test_data import POSITIVE_SEARCH_QUERIES, NEGATIVE_SEARCH_QUERIES, INVALID_METHOD_SEARCH

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}

@allure.feature("API")
class TestSearchAPI:

    @allure.story("Успешный поиск по точному названию товара")
    @allure.step("Поиск по запросу: {query}")
    @pytest.mark.parametrize("query", POSITIVE_SEARCH_QUERIES)
    def test_positive_search(self, query):
        response = requests.post(f"{API_BASE_URL}/search/results", headers=HEADERS, json=query)
        assert response.status_code == 204, f"Ожидался статус-код 204, но получен {response.status_code}"
        # Проверка, что тело ответа пустое
        assert response.text == "", "Ожидалось пустое тело ответа для статус-кода 204"

    @allure.story("Поиск с пустым запросом")
    @allure.step("Поиск с пустым запросом")
    def test_empty_search(self):
        query = NEGATIVE_SEARCH_QUERIES[0]
        response = requests.post(f"{API_BASE_URL}/search/results", headers=HEADERS, json=query)
        assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"
        response_json = response.json()
        assert "errors" in response_json, "Ожидалась ошибка для пустого запроса"
        assert response_json["errors"][0]["title"] == "Значение не должно быть пустым.", "Некорректное сообщение об ошибке"

    @allure.story("Поиск с запросом специальных символов")
    @allure.step("Поиск с запросом специальных символов")
    def test_special_characters_search(self):
        query = NEGATIVE_SEARCH_QUERIES[1]
        response = requests.post(f"{API_BASE_URL}/search/results", headers=HEADERS, json=query)
        assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"#баг, код должен возвращаться 422, а возвращается 204
        response_json = response.json()
        assert "errors" in response_json, "Ожидалась ошибка для запроса со специальными символами"
        assert response_json["errors"][0]["title"] == "Значение не должно быть пустым.", "Некорректное сообщение об ошибке"

    @allure.story("Поиск с использованием эмодзи")
    @allure.step("Поиск с использованием эмодзи")
    def test_emoji_search(self):
        query = NEGATIVE_SEARCH_QUERIES[2]
        response = requests.post(f"{API_BASE_URL}/search/results", headers=HEADERS, json=query)
        assert response.status_code == 422, f"Ожидался статус-код 422, но получен {response.status_code}"#баг, код должен возвращаться 422, а возвращается 204
        response_json = response.json()
        assert "errors" in response_json, "Ожидалась ошибка для запроса с эмодзи"
        assert response_json["errors"][0]["title"] == "Значение не должно быть пустым.", "Некорректное сообщение об ошибке"

    @allure.story("Поиск с использованием неверного метода запроса")
    @allure.step("Поиск с использованием неверного метода запроса")
    def test_invalid_method_search(self):
        response = requests.get(f"{API_BASE_URL}/search/results", headers=HEADERS, json=INVALID_METHOD_SEARCH)
        assert response.status_code == 405, f"Ожидался статус-код 405, но получен {response.status_code}"
        assert "method not allowed" in response.text.lower(), "Ожидалась ошибка для неверного метода запроса"
