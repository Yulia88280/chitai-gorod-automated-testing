# Chitai-Gorod Automated Testing

## Описание

Проект предназначен для автоматизированного тестирования сайта "Читай-город".[Читай-город](https://www.chitai-gorod.ru/).

## Структура проекта

- `config/` - Конфигурационные файлы и тестовые данные.
- `pages/` - Реализация Page Object Model (POM).
- `tests/` - Тесты (UI и API).
- `utils/` - Вспомогательные утилиты.
- `requirements.txt` - Зависимости проекта.
- `README.md` - Описание проекта.

## Перейдите в каталог проекта:
cd chitai-gorod-automated-testing

## Зависимости
Selenium
Requests
Pytest
Allure

## Настройка
### Установите зависимости:
Selenium  pip install selenium
Requests  pip install requests
Pytest    pip install pytest
Allure    pip install allure-pytest

## Запуск тестов

Чтобы запустить только UI тесты:
```bash
pytest tests/test_ui.py

Чтобы запустить только API тесты:
pytest tests/test_api.py

Чтобы запустить все тесты:
pytest tests/

Чтобы запустит Allure:
pytest --alluredir allure-result

Открыть отчет Allure:
allure serve allure-result
## Ссылка на проект
[Финальный проект по ручному тестированию] (https://responsible-bean-1e3.notion.site/e5002d855e4343159bf8fb08e4bc6340)

