import allure

from pages.orders_list_page import OrdersList

class TestOrdersList:

    @allure.title("Проверка успешного перехода в окно описания заказа в разделе Лента заказов кликом позиции заказа")
    @allure.description("В ленте заказов кликнуть по заказу и проверить, что произошел переход окно описания заказа")
    def test_moving_to_orders_list_window(self, driver):
        orders_list = OrdersList(driver)
        orders_list.click_orders_list_link()
        orders_list.click_oder_in_orders_list()
        assert orders_list.check_text_in_order_description_window() == 'Cостав'

    @allure.title("Проверка успешной регистрации созданного авторизованных пользователем заказа в ленте заказов")
    @allure.description("Авторизоваться пользователем, создать новый заказ, проверить, что новый заказ отобразился как в истории заказов, так и в ленте заказов")
    def test_order_registration_in_history_and_orders_list(self,  driver, generate_user):
        email, password = generate_user
        orders_list = OrdersList(driver)
        orders_list.user_authorization(email, password)
        orders_list.drag_bread_to_basket()
        orders_list.scroll_to_sauce()
        orders_list.drag_sauce_to_basket()
        orders_list.click_order_button()
        orders_list.click_order_description_close_button()
        orders_list.click_account_button()
        orders_list.click_orders_history_button()
        orders_list.scroll_to_order()
        orders_list.click_order_in_order_history()
        order_number_history = orders_list.check_number_in_order_history_window()
        orders_list.click_order_description_close_button()
        orders_list.click_orders_list_link()
        orders_list.click_oder_in_orders_list()
        order_number_in_list = orders_list.check_number_in_order_list_window()
        assert order_number_history == order_number_in_list

    @allure.title("Проверка успешного обновления счетчика заказов, выполненных за все время")
    @allure.description("Авторизоваться пользователем, создать новый заказ, проверить, количество заказов в счетчике всех выполненных заказов увеличилось на один")
    def test_all_orders_counter(self, driver, generate_user):
        email, password = generate_user
        orders_list = OrdersList(driver)
        orders_list.user_authorization(email, password)
        orders_list.click_orders_list_link()
        original_number = orders_list.check_text_in_all_orders_counter()
        orders_list.click_constructor_link()
        orders_list.drag_bread_to_basket()
        orders_list.scroll_to_sauce()
        orders_list.drag_sauce_to_basket()
        orders_list.click_order_button()
        orders_list.click_order_description_close_button()
        orders_list.click_orders_list_link()
        new_number = orders_list.check_text_in_all_orders_counter()
        assert new_number == original_number + 1

    @allure.title("Проверка успешного обновления счетчика заказов, выполненных за сегодня")
    @allure.description("Авторизоваться пользователем, создать новый заказ, проверить, что количество заказов, выполненных за сегодня, в счетчике увеличилось на один")
    def test_today_orders_counter(self, driver, generate_user):
        email, password = generate_user
        orders_list = OrdersList(driver)
        orders_list.user_authorization(email, password)
        orders_list.click_orders_list_link()
        orders_list.scroll_to_today_counter()
        original_number = orders_list.check_text_in_today_orders_counter()
        orders_list.click_constructor_link()
        orders_list.drag_bread_to_basket()
        orders_list.scroll_to_sauce()
        orders_list.drag_sauce_to_basket()
        orders_list.click_order_button()
        orders_list.click_order_description_close_button()
        orders_list.click_orders_list_link()
        orders_list.scroll_to_today_counter()
        new_number = orders_list.check_text_in_today_orders_counter()
        assert new_number == original_number + 1

    @allure.title("Проверка успешной регистрации созданного авторизованных пользователем заказа в разделе В работе")
    @allure.description("Авторизоваться пользователем, создать новый заказ, проверить, что новый заказ отобразился в ленте заказов в разделе В работе")
    def test_order_registration_in_preparing_orders(self, driver, generate_user):
        email, password = generate_user
        orders_list = OrdersList(driver)
        orders_list.user_authorization(email, password)
        orders_list.drag_bread_to_basket()
        orders_list.scroll_to_sauce()
        orders_list.drag_sauce_to_basket()
        orders_list.click_order_button()
        new_order_number = orders_list.check_new_order_number()
        orders_list.click_order_description_close_button()
        orders_list.click_orders_list_link()
        order_number_preparing = orders_list.check_order_number_in_preparing()
        assert new_order_number == order_number_preparing
