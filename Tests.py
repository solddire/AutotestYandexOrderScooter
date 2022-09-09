import allure

from PageObject import Main_Page, Form_Order, About_Rent
from selenium.webdriver.common.by import By


# Создаем тестовый класс и методы
class TestProgram:
    @allure.title('Тест кнопки заказать')
    @allure.feature('Test button')
    @allure.story('Проверяем кнопку заказать')
    def test_click_button(self, browser):
        first_question = Main_Page(browser)  # Создаем экземпляр класса first_question
        first_question.go_to_site()  # Запускаем сайт, это делается только один раз!
        first_question.click_to_order()

    @allure.title('Заполнение имени')
    @allure.feature('Filling out name')
    @allure.story('Заполняем имя и фамилию')
    def test_fill_out_name(self, browser):
        write_in_name = Form_Order(browser)
        write_in_name.fill_name()

    @allure.title('Заполнение адреса')
    @allure.feature('Filling out address')
    @allure.story('Заполняем адрес')
    def test_fill_out_address(self, browser):
        write_in_address = Form_Order(browser)
        write_in_address.fill_address()

    @allure.title('Заполнение телефона')
    @allure.feature('Filling out phone number')
    @allure.story('Заполняем номер телефона')
    def test_fill_out_phone(self, browser):
        write_in_phone = Form_Order(browser)
        write_in_phone.fill_phone()

    @allure.title('Проверка заполнения данных')
    @allure.feature('Checking the filling of data')
    @allure.story('Проверяем, что заполнили данные')
    def test_check_order(self, browser):
        test = browser.find_element(By.CLASS_NAME, "Order_Header__BZXOb")
        assert test.text == "Про аренду"

    @allure.title('Заполнение "про аренду"')
    @allure.feature('Fill "about rent"')
    @allure.story('Заполняем "про аренду"')
    def test_fill_rent(self, browser):
        write_in_rent = About_Rent(browser)
        write_in_rent.fill_date()
        write_in_rent.fill_other()

    @allure.title('Проверка оформления заказа')
    @allure.feature('Fill "for rent"')
    @allure.story('Заполняем "про аренду"')
    def test_check_exe_of_the_order(self, browser):
        test = browser.find_element(By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
        assert test.text == "Заказ оформлен"
