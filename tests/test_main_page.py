import allure

from pages.main_page import MainPage
from curl import *

class TestMainPageFunctions:

    @allure.title("Проверка успешного перехода авторизованного пользователя в раздел Лента заказов кликом по кнопке Лента заказов")
    @allure.description("На главной странице кликнуть по кнопке Лента заказов и проверить, что произошел переход в раздел ленты заказов")
    def test_moving_to_orders_list_section(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_list_link()
        assert driver.current_url == Url.ORDERS_LIST

    @allure.title("Проверка успешного перехода авторизованного пользователя в раздел Конструктор кликом по кнопке Конструктор")
    @allure.description("На главной странице кликнуть по кнопке Лента заказов, затем кликнуть по кнопке Конструктор, и проверить, что произошел переход в раздел Конструктор")
    def test_constructor_section(self, driver):
        main_page = MainPage(driver)
        main_page.click_orders_list_link()
        main_page.click_constructor_link()
        assert driver.current_url == Url.MAIN_SITE

    @allure.title("Проверка успешного перехода в окно описания ингредиента кликом по ингредиенту в конструкторе")
    @allure.description("В конструкторе бургеров кликнуть по ингредиенту, проверить, что открылось окно с описанием ингредиента")
    def test_ingredient_description(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        assert main_page.check_text_in_ingredient_description_window() == 'Детали ингредиента'

    @allure.title("Проверка успешного закрытия окна описания ингредиента кликом крестику в правом верхнем углу окна")
    @allure.description("В окне описания ингредиента кликнуть по кнопке в виде крестика, проверить, что окно закрылось и стал виден заголовок раздела конструктор")
    def test_ingredient_description_window_close(self, driver):
        main_page = MainPage(driver)
        main_page.click_ingredient()
        main_page.click_ingredient_description_close_button()
        assert main_page.check_text_in_constructor_title() == 'Соберите бургер'

    @allure.title("Проверка изменения значения каунтера ингредиента при его добавлении в корзину")
    @allure.description("Перетащить соус в корзину и проверить, что его каунтер увеличился на единицу")
    def test_change_count_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_sauce()
        initial_count = main_page.check_text_in_counter()
        main_page.drag_sauce_to_basket()
        new_count = main_page.check_text_in_counter()
        assert new_count == initial_count + 1

    @allure.title("Проверка возможности создания заказа авторизованным пользователем")
    @allure.description("Перетащить булку и соус в корзину, нажать кнопку Оформить заказ и проверить, что открылось окно с номером заказа")
    def test_create_order_by_authorized_user(self, driver, generate_user):
        email, password = generate_user
        main_page = MainPage(driver)
        main_page.user_authorization(email, password)
        main_page.drag_bread_to_basket()
        main_page.scroll_to_sauce()
        main_page.drag_sauce_to_basket()
        main_page.click_order_button()
        assert main_page.check_text_in_order_window() == 'идентификатор заказа'

