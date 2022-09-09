import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox()  # Здесь мы задаем браузер, делаем как я в данном случае, "полный" экран
    driver.maximize_window()  # Yield это ключевое слово, которое используется примерно как return — отличие в
    yield driver  # том, что функция вернёт генератор.
    driver.quit()  # В conftest происходит инициализация webdriver с указанием где располагается geckodriver.
    # Далее используем конструкцию yield,
    # которая разделяет функцию на часть — до тестов и после тестов.

    # В части “после тестов” мы вызываем функцию quit, которая завершает сессию и
    # убивает экземпляр webdriver.
