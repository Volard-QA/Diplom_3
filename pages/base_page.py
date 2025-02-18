import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


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

    @allure.step("Ожидание прогрузки страницы")
    def wait_for_page_load(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    @allure.step("Получение Url текущей страницы")
    def get_current_url(self):
        return self.driver.current_url

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
