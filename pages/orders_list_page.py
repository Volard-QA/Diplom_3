import allure

from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from locators.orders_list_locators import OrdersListLocators

class OrdersList(BasePage):

    @allure.step("Клик по заказу в ленте заказов")
    def click_oder_in_orders_list(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(OrdersListLocators.ORDER_IN_LIST)

    @allure.step("Получение текста Состав в окне описания заказа")
    def check_text_in_order_description_window(self):
        self.wait_element(OrdersListLocators.ORDER_DESCRIPTION_WINDOW)
        return self.get_text_in_element(OrdersListLocators.ORDER_DESCRIPTION_WINDOW)

    @allure.step("Клик по кнопке Лента заказов в шапке")
    def click_orders_list_link(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ORDERS_LIST_LINK)

    @allure.step("Авторизация пользователя")
    def user_authorization(self, email, password):
        self.login_user(email, password)

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

    @allure.step("Кликнуть по кнопке Оформить заказ")
    def click_order_button(self):
        self.click_on_element(BasePageLocators.ORDER_BUTTON)

    @allure.step("Клик по кнопке закрытия окна заказа")
    def click_order_description_close_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.DESCRIPTION_CLOSE_BUTTON)

    @allure.step("Клик по кнопке Личный кабинет на главной странице")
    def click_account_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ACCOUNT_BUTTON)
        self.wait_for_profile_page_load()

    @allure.step("Получение номера заказа в окне заказа в разделе истории заказов")
    def check_number_in_order_history_window(self):
        self.wait_element(OrdersListLocators.ORDER_NUMBER_IN_ORDER_HISTORY_WINDOW)
        element = self.find_element(OrdersListLocators.ORDER_NUMBER_IN_ORDER_HISTORY_WINDOW)
        return element.text.replace('"', '').replace('\n', '')

    @allure.step("Получение номера заказа в окне описания заказа в ленте заказов")
    def check_number_in_order_list_window(self):
        self.wait_element(OrdersListLocators.ORDER_NUMBER_IN_ORDER_LIST_WINDOW)
        return self.get_text_in_element(OrdersListLocators.ORDER_NUMBER_IN_ORDER_LIST_WINDOW)

    @allure.step("Клик по кнопке История заказов на странице профиля пользователя")
    def click_orders_history_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ORDERS_HISTORY_BUTTON)
        self.wait_for_order_history_page_load()

    @allure.step("Проскроллить до значения Заказа в Истории заказа")
    def scroll_to_order(self):
        self.scroll_to_element(OrdersListLocators.ORDER_IN_ORDER_HISTORY_WINDOW)

    @allure.step("Клик по заказу в истории заказов")
    def click_order_in_order_history(self):
        self.click_on_element(OrdersListLocators.ORDER_IN_ORDER_HISTORY_WINDOW)

    @allure.step("Проверить число заказов в счетчике всех выполненных заказов")
    def check_text_in_all_orders_counter(self):
        self.wait_element(OrdersListLocators.NUMBER_IN_ALL_ORDERS_COUNTER)
        return int(self.get_text_in_element(OrdersListLocators.NUMBER_IN_ALL_ORDERS_COUNTER))

    @allure.step("Клик по кнопке Конструктор в шапке")
    def click_constructor_link(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.CONSTRUCTOR_LINK)

    @allure.step("Проверить число заказов в счетчике заказов, выполненных за сегодня")
    def check_text_in_today_orders_counter(self):
        self.wait_element(OrdersListLocators.NUMBER_IN_TODAY_ORDERS_COUNTER)
        return int(self.get_text_in_element(OrdersListLocators.NUMBER_IN_TODAY_ORDERS_COUNTER))

    @allure.step("Проскроллить до счетчика сегодняшних заказов")
    def scroll_to_today_counter(self):
        self.scroll_to_element(OrdersListLocators.NUMBER_IN_TODAY_ORDERS_COUNTER)

    @allure.step("Проверить номер нового заказа")
    def check_new_order_number(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.wait_element(OrdersListLocators.ORDER_NUMBER_IN_ORDER_CREATION_WINDOW)
        return f'0{self.get_text_in_element(OrdersListLocators.ORDER_NUMBER_IN_ORDER_CREATION_WINDOW)}'

    @allure.step("Проверить номер нового заказа в разделе В работе")
    def check_order_number_in_preparing(self):
        self.wait_element(OrdersListLocators.NUMBER_IN_PREPARING_ORDERS)
        return self.get_text_in_element(OrdersListLocators.NUMBER_IN_PREPARING_ORDERS)
