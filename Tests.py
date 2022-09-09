import allure
from selenium.webdriver.common.by import By

from PageObject import Main_Page, Form_Order, About_Rent, YandexButton


# Создаем тестовый класс и методы
class TestProgram:
    @allure.title('Тест кнопки заказать')
    @allure.feature('Test button')
    @allure.story('Проверяем кнопку заказать')
    def test_click_button_top(self, browser):
        main = Main_Page(browser)  # Создаем экземпляр класса main.
        main.go_to_site()  # Запускаем сайт, это делается только один раз!
        main.click_to_order_top()  # Нажимаем на кнопку заказать.

    @allure.title('Заполнение имени')
    @allure.feature('Filling out name')
    @allure.story('Заполняем имя и фамилию')
    def test_fill_out_name(self, browser):
        write_in_name = Form_Order(browser)  # Создаем экземпляр класса write_in_name.
        write_in_name.fill_name()  # Заполняем данным методом имя и фамилию.

    @allure.title('Заполнение адреса')
    @allure.feature('Filling out address')
    @allure.story('Заполняем адрес')
    def test_fill_out_address(self, browser):
        write_in_address = Form_Order(browser)  # Создаем экземпляр класса write_in_address.
        write_in_address.fill_address()  # Заполняем данным методом адрес и метро.

    @allure.title('Заполнение телефона')
    @allure.feature('Filling out phone number')
    @allure.story('Заполняем номер телефона')
    def test_fill_out_phone(self, browser):
        write_in_phone = Form_Order(browser)  # Создаем экземпляр класса write_in_phone.
        write_in_phone.fill_phone()  # Заполняем данным методом телефон, нажимаем на кнопку.

    @allure.title('Проверка заполнения данных')
    @allure.feature('Checking the filling of data')
    @allure.story('Проверяем, что заполнили данные')
    def test_check_order(self, browser):
        test = browser.find_element(By.CLASS_NAME,
                                    "Order_Header__BZXOb")  # В данном методе проверяем, что мы перешли в следующее
        # окно (Про Аренду).
        assert test.text == "Про аренду"

    @allure.title('Заполнение "про аренду"')
    @allure.feature('Fill "about rent"')
    @allure.story('Заполняем "про аренду"')
    def test_fill_rent(self, browser):
        write_in_rent = About_Rent(browser)  # Создаем экземпляр класса write_in_rent.
        write_in_rent.fill_date()  # Заполняем данным методом дату.
        write_in_rent.fill_other()  # Заполняем цвет, комментарий, и нажимаем кнопку заказать, подтверждаем заказ.

    @allure.title('Проверка оформления заказа(верхняя кнопка)')
    @allure.feature('Fill "for rent"(top button)')
    @allure.story('Проверяем оформление заказа(верхняя кнопка)')
    def test_check_exe_of_the_order(self, browser):
        check = About_Rent(browser)  # Создаем экземпляр класса check.
        test = browser.find_element(By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                     "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                                     "button.Button_Button__ra12g.Button_Middle__1CSJM")  # Ищу
        # кнопку, так как текст динамичен, и номер заказа не предугадать.
        assert test.text == "Посмотреть статус"  # Проверяем по тексту с кнопки.
        check.check_status()  # Нажимаем на кнопку "Проверить статус".

    @allure.title('Проверка кнопок Яндекса')
    @allure.feature('Check Yandex buttons')
    @allure.story('Проверяем кнопки Яндекса"')
    def test_yandex_buttons(self, browser):
        click = YandexButton(browser)  # Создаем экземпляр класса click.
        click.click_on_yandex_button()  # Нажимаем на кнопку "Яндекс".
        browser.switch_to_window(browser.window_handles[1])  # Переключаемся на страницу "Яндекса".
        url = browser.current_url  # Берем текущий url, чтобы сверить, верно ли все произошло.
        assert url == 'https://yandex.ru/'  # Сравниваем url'ы.
        browser.close()  # Закрываем окно "Яндекс".
        browser.switch_to_window(browser.window_handles[0])  # Переходим обратно в "основное" окно.
        url = browser.current_url  # Берем текущий url, чтобы сверить, верно ли все произошло.
        click.click_on_scooter_button()  # Нажимаем на кнопку "Самокаты".
        assert url == 'https://qa-scooter.praktikum-services.ru/'  # Сравниваем url'ы.

    @allure.title('Проверка кнопки заказа(нижняя)')
    @allure.feature('Check button(down)')
    @allure.story('Проверяем кнопку заказ(нижняя)"')
    def test_order_form_down(self, browser):
        order_form = Main_Page(browser)  # Создаем экземпляр класса order_form.
        element = browser.find_element(By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")  # Кнопка "Заказать" нижняя.
        browser.execute_script("arguments[0].scrollIntoView();", element)  # Здесь пришлось делать скрипт, для того
        # чтобы страница скроллилась вниз, до нашего элемента!
        order_form.click_to_order_down()  # Нажимаем на кнопку заказать.
        fill_form = Form_Order(browser)  # Создаем экземпляр класса fill_form
        fill_form.fill_name()  # Заполняем данным методом имя и фамилию.
        fill_form.fill_address()  # Заполняем данным методом адрес и метро.
        fill_form.fill_phone()  # Заполняем данным методом телефон, нажимаем на кнопку.
        test = browser.find_element(By.CLASS_NAME, "Order_Header__BZXOb") # Проверяем, что мы перешли в следующее
        # окно (Про Аренду).
        assert test.text == "Про аренду"

    @allure.title('Проверка оформления заказа(нижняя кнопка) ')
    @allure.feature('Fill "for rent"(down)')
    @allure.story('Проверяем оформление заказа(нижняя кнопка)"')
    def test_about_rent_down(self, browser):
        write_in_rent = About_Rent(browser)  # Создаем экземпляр класса write_in_rent.
        write_in_rent.fill_date()  # Заполняем данным методом дату.
        write_in_rent.fill_other()  # Заполняем цвет, комментарий, и нажимаем кнопку заказать, подтверждаем заказ.
        check = About_Rent(browser)  # Создаем экземпляр класса check.
        test = browser.find_element(By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                     "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                                     "button.Button_Button__ra12g.Button_Middle__1CSJM")# Ищу
        # кнопку, так как текст динамичен, и номер заказа не предугадать.
        assert test.text == "Посмотреть статус"  # Проверяем по тексту с кнопки.
        check.check_status()  # Нажимаем на кнопку "Проверить статус".
