from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:  # В классе BasePage определяем базовые методы для работы с WebDriver.
    # В классе BasePage создаем конструктор, который принимает driver — экземпляр webdriver.
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru"  # Указываем base_url,
        self.quantity = 0  # который будет использоваться для открытия страницы.

    def driverwait(self, locator):
        return WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(locator))

    # Это обертка над WebdriverWait, который отвечает за явные ожидания в Selenium.
    def go_to_site(self):
        return self.driver.get(self.base_url)
    # Метод go_to_site — вызывает функцию get из WebDriver. Метод позволяет перейти на указываемую страницу.
    # Передаем в него base_url.
