from BaseApp import BasePage
from selenium.webdriver.common.by import By


# Создаем класс FireFoxLocators. Он будет только для хранения локаторов.
# В классе описываем локаторы:
class FireFoxLocators:
    LOCATOR_COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    LOCATOR_TOP_ORDER_BUTTON = (By.CLASS_NAME, "Button_Button__ra12g")
    LOCATOR_NAME_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u div."
                                          "Input_InputContainer__3NykH:nth-child(1) > input.Input_Input__1iN_Z."
                                          "Input_Responsible__1jDKN")
    LOCATOR_LASTNAME_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u"
                                              " div.Input_InputContainer__3NykH:nth-child(2) > "
                                              "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")
    LOCATOR_ADDRESS_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u "
                                             "div.Input_InputContainer__3NykH:nth-child(3) > "
                                             "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")
    LOCATOR_METRO_FORM_BUTTON = (By.CLASS_NAME, "select-search__input")
    LOCATOR_METRO_FORM_CHOICE = (By.XPATH, "//input[@class='select-search__input']")
    LOCATOR_PHONE_FORM = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Form__17u6u "
                                           "div.Input_InputContainer__3NykH:nth-child(5) > "
                                           "input.Input_Input__1iN_Z.Input_Responsible__1jDKN")
    LOCATOR_CONTINUE_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__15LM- div.Order_Content__bmtHS "
                                                "div.Order_NextButton__1_rCA > "
                                                "button.Button_Button__ra12g.Button_Middle__1CSJM")
    LOCATOR_METRO_SQUARE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[3]/button")
    LOCATOR_DATE_BRING_SCOOTER = (By.XPATH, "//div[@class='react-datepicker__input-container']//input[@type='text']")
    LOCATOR_DATE_BRING_SCOOTER_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS "
                                                          "div.Order_Form__17u6u div.Order_MixedDatePicker__3qiay "
                                                          "div.react-datepicker__tab-loop div.react-datepicker-popper "
                                                          "div.react-datepicker "
                                                          "div.react-datepicker__month-container:nth-child(4) "
                                                          "div.react-datepicker__month "
                                                          "div.react-datepicker__week:nth-child(3) > "
                                                          "div.react-datepicker__day.react-datepicker__day--018.react"
                                                          "-datepicker__day--weekend:nth-child(7)")
    LOCATOR_RENTAL_PERIOD_BUTTON = (By.XPATH, "//div[@class='Dropdown-control']")
    LOCATOR_RENTAL_PERIOD_CHOICE = (By.CSS_SELECTOR, "div.Dropdown-option:nth-child(1)")
    LOCATOR_COLOR_SCOOTER = (By.CLASS_NAME, "Checkbox_Input__14A2w")
    LOCATOR_COMMENTARY = (By.XPATH, "//div[@class='Order_Form__17u6u']//div["
                                    "@class='Input_InputContainer__3NykH']//input[@type='text']")
    LOCATOR_ORDER_BUTTON = (By.CSS_SELECTOR, "div:nth-child(2) div.App_App__15LM- div.Order_Content__bmtHS "
                                             "div.Order_Buttons__1xGrp > "
                                             "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")
    LOCATOR_CONFIRM_BUTTON = (By.CSS_SELECTOR, "div.App_App__15LM- div.Order_Content__bmtHS div.Order_Modal__YZ-d3 "
                                               "div.Order_Buttons__1xGrp > "
                                               "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-child(2)")
    LOCATOR_CHECK_STATUS = (By.CLASS_NAME, "//button[contains(text(),'Посмотреть статус')]")


# Создаем класс Question_Program, наследуемся от BasePage.
class Main_Page(BasePage):
    def click_to_order(self):
        self.driverwait(FireFoxLocators.LOCATOR_COOKIE_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_TOP_ORDER_BUTTON).click()

    # В данных методах реализуем нажатие на кнопки.
    # P.S. В первом методе больше кликов, потому что кнопка куки мешает для нажатия.


class Form_Order(BasePage):
    def fill_name(self):
        self.driverwait(FireFoxLocators.LOCATOR_NAME_FORM).send_keys('Алексей')
        self.driverwait(FireFoxLocators.LOCATOR_LASTNAME_FORM).send_keys('Великолепный')

    def fill_address(self):
        self.driverwait(FireFoxLocators.LOCATOR_ADDRESS_FORM).send_keys('Улица Маршала Бирюзова, дом 42')
        self.driverwait(FireFoxLocators.LOCATOR_METRO_FORM_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_METRO_SQUARE_BUTTON).click()

    def fill_phone(self):
        self.driverwait(FireFoxLocators.LOCATOR_PHONE_FORM).send_keys('89612653265')
        self.driverwait(FireFoxLocators.LOCATOR_CONTINUE_BUTTON).click()


class About_Rent(BasePage):
    def fill_date(self):
        self.driverwait(FireFoxLocators.LOCATOR_DATE_BRING_SCOOTER).send_keys('18.09.2022')
        self.driverwait(FireFoxLocators.LOCATOR_DATE_BRING_SCOOTER_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_RENTAL_PERIOD_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_RENTAL_PERIOD_CHOICE).click()

    def fill_other(self):
        self.driverwait(FireFoxLocators.LOCATOR_COLOR_SCOOTER).click()
        self.driverwait(FireFoxLocators.LOCATOR_COMMENTARY).send_keys('Привести к 18:00.')
        self.driverwait(FireFoxLocators.LOCATOR_ORDER_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_CONFIRM_BUTTON).click()
        self.driverwait(FireFoxLocators.LOCATOR_CHECK_STATUS).click()
