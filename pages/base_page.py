import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from curl import *
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Ожидать видимость элемента")
    def wait_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элемент")
    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    @allure.step("Скролл до нужного элемента")
    def scroll_to_element(self, locator, timeout=10):
        element = self.wait_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть по элементу")
    def click_on_element(self, locator, timeout=10):
        element = self.wait_element(locator, timeout)
        element.click()

    @allure.step("Ввести текст в поле")
    def insert_keys_into_input(self, locator, keys, timeout=10):
        element = self.wait_element(locator, timeout)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст из элемента")
    def get_text_in_element(self, locator, timeout=10):
        self.wait_element(locator, timeout)
        element = self.find_element(locator)
        return element.text

    @allure.step("Ожидать пока элемент станет невидимым")
    def wait_for_element_to_hide(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидание прогрузки страницы восстановления пароля")
    def wait_for_recover_page_load(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Url.PASSWORD_RECOVERY_PAGE))

    @allure.step("Ожидание прогрузки страницы сброса пароля")
    def wait_for_reset_page_load(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Url.PASSWORD_RESET_PAGE))

    @allure.step("Ожидание прогрузки страницы профиля пользователя")
    def wait_for_profile_page_load(self, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Url.PROFILE_PAGE))

    @allure.step("Ожидание прогрузки страницы истории заказов")
    def wait_for_order_history_page_load(self, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Url.USER_ORDERS_PAGE))

    @allure.step("Ожидание прогрузки страницы авторизации")
    def wait_for_login_page_load(self, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Url.LOGIN_PAGE))

    @allure.step("Ожидание прогрузки главной страницы")
    def wait_for_main_page_load(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Url.MAIN_SITE))

    @allure.step("Ожидание прогрузки ленты заказов")
    def wait_for_orders_list_load(self, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(Url.ORDERS_LIST))


    @allure.step("Авторизация пользователя в приложении")
    def login_user(self, email, password):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ACCOUNT_BUTTON)
        self.wait_for_login_page_load()
        self.click_on_element(LoginPageLocators.EMAIL_FIELD)
        self.insert_keys_into_input(LoginPageLocators.EMAIL_FIELD_ACTIVE, email)
        self.click_on_element(LoginPageLocators.PASSWORD_FIELD)
        self.insert_keys_into_input(LoginPageLocators.PASSWORD_FIELD_ACTIVE, password)
        self.click_on_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Перетащить элемент в корзину")
    def drag_and_drop_element(self, source, target):
        source_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(source)
        )
        target_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(target)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", source_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", target_element)
        self.driver.execute_script("""
                function createEvent(typeOfEvent) {
                    var event = document.createEvent("CustomEvent");
                    event.initCustomEvent(typeOfEvent, true, true, null);
                    event.dataTransfer = {
                        data: {},
                        setData: function(key, value) {
                            this.data[key] = value;
                        },
                        getData: function(key) {
                            return this.data[key];
                        }
                    };
                    return event;
                }

                function dispatchEvent(element, event, transferData) {
                    if (transferData !== undefined) {
                        event.dataTransfer = transferData;
                    }
                    if (element.dispatchEvent) {
                        element.dispatchEvent(event);
                    } else if (element.fireEvent) {
                        element.fireEvent("on" + event.type, event);
                    }
                }

                function simulateHTML5DragAndDrop(element, target) {
                    var dragStartEvent = createEvent('dragstart');
                    dispatchEvent(element, dragStartEvent);

                    var dropEvent = createEvent('drop');
                    dispatchEvent(target, dropEvent);

                    var dragEndEvent = createEvent('dragend');
                    dispatchEvent(element, dragEndEvent);
                }

                simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """, source_element, target_element)
