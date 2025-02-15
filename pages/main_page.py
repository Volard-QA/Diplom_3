import allure

from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Авторизация пользователя")
    def user_authorization(self, email, password):
        self.login_user(email, password)

    @allure.step("Клик по кнопке Конструктор в шапке")
    def click_constructor_link(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Клик по кнопке Лента заказов в шапке")
    def click_orders_list_link(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ORDERS_LIST_LINK)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(MainPageLocators.INGREDIENT_LOCATOR)

    @allure.step("Получение текста заголовка в окне описания ингредиента")
    def check_text_in_ingredient_description_window(self):
        self.wait_element(MainPageLocators.INGREDIENT_DESCRIPTION_TITLE)
        return self.get_text_in_element(MainPageLocators.INGREDIENT_DESCRIPTION_TITLE)

    @allure.step("Клик по кнопке закрытия окна описания ингредиентов")
    def click_ingredient_description_close_button(self):
        self.click_on_element(BasePageLocators.DESCRIPTION_CLOSE_BUTTON)

    @allure.step("Получение текста заголовка конструктора")
    def check_text_in_constructor_title(self):
        self.wait_element(MainPageLocators.CONSTRUCTOR_TITLE_TEXT)
        return self.get_text_in_element(MainPageLocators.CONSTRUCTOR_TITLE_TEXT)

    @allure.step("Проскроллить до первого значения Соуса в Конструкторе")
    def scroll_to_sauce(self):
        self.scroll_to_element(BasePageLocators.SAUCE)

    @allure.step("Перетащить ингредиент соус в козину")
    def drag_sauce_to_basket(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.drag_and_drop_element(BasePageLocators.SAUCE, BasePageLocators.BASKET)

    @allure.step("Перетащить ингредиент булку в козину")
    def drag_bread_to_basket(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.drag_and_drop_element(BasePageLocators.BREAD, BasePageLocators.BASKET)


    @allure.step("Получить текст каунтера соуса")
    def check_text_in_counter(self):
        self.wait_element(MainPageLocators.COUNTER)
        return int(self.get_text_in_element(MainPageLocators.COUNTER))

    @allure.step("Кликнуть по кнопке Оформить заказ")
    def click_order_button(self):
        self.click_on_element(BasePageLocators.ORDER_BUTTON)

    @allure.step("Проверить наличие текста идентификатор заказа")
    def check_text_in_order_window(self):
        self.wait_element(MainPageLocators.ORDER_WINDOW_TEXT)
        return self.get_text_in_element(MainPageLocators.ORDER_WINDOW_TEXT)
