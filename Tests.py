import allure
from selenium.webdriver.common.by import By

from PageObject import Main_Page, Form_Order, About_Rent, YandexButton


# Создаем тестовый класс и методы
class TestProgram:
    @allure.title('Тест кнопки заказать')
    @allure.feature('Test button')
    @allure.story('Проверяем кнопку заказать')
    def test_click_button_top(self, browser):
        main = Main_Page(browser)  # Создаем экземпляр класса first_question
        main.go_to_site()  # Запускаем сайт, это делается только один раз!
        main.click_to_order_top()

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

    @allure.title('Проверка оформления заказа(верхняя кнопка)')
    @allure.feature('Fill "for rent"(top button)')
    @allure.story('Проверяем оформление заказа(верхняя кнопка)')
    def test_check_exe_of_the_order(self, browser):
        check = About_Rent(browser)
        test = browser.find_element(By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                     "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                                     "button.Button_Button__ra12g.Button_Middle__1CSJM")
        assert test.text == "Посмотреть статус"
        check.check_status()

    @allure.title('Проверка кнопок Яндекса')
    @allure.feature('Check Yandex buttons')
    @allure.story('Проверяем кнопки Яндекса"')
    def test_yandex_buttons(self, browser):
        click = YandexButton(browser)
        click.click_on_scooter_button()
        click.click_on_yandex_button()
        browser.switch_to_window(browser.window_handles[1])
        browser.close()
        browser.switch_to_window(browser.window_handles[0])

    @allure.title('Проверка кнопки заказа(нижняя)')
    @allure.feature('Check button(down)')
    @allure.story('Проверяем кнопку заказ(нижняя)"')
    def test_order_form_down(self, browser):
        order_form = Main_Page(browser)
        element = browser.find_element(By.XPATH, "//button[@class='Button_Button__ra12g Button_UltraBig__UU3Lp']")
        browser.execute_script("arguments[0].scrollIntoView();", element)  # Здесь пришлось делать скрипт, для того
        # чтобы страница скроллилась вниз, иначе все это не работает!!
        order_form.click_to_order_down()
        fill_form = Form_Order(browser)
        fill_form.fill_name()
        fill_form.fill_address()
        fill_form.fill_phone()
        test = browser.find_element(By.CLASS_NAME, "Order_Header__BZXOb")
        assert test.text == "Про аренду"

    @allure.title('Проверка оформления заказа(нижняя кнопка) ')
    @allure.feature('Fill "for rent"(down)')
    @allure.story('Проверяем оформление заказа(нижняя кнопка)"')
    def test_about_rent_down(self, browser):
        write_in_rent = About_Rent(browser)
        write_in_rent.fill_date()
        write_in_rent.fill_other()
        check = About_Rent(browser)
        test = browser.find_element(By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                     "div.Order_Modal__YZ-d3 div.Order_NextButton__1_rCA > "
                                                     "button.Button_Button__ra12g.Button_Middle__1CSJM")
        assert test.text == "Посмотреть статус"
        check.check_status()
