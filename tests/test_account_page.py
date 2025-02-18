import allure

from pages.account_page import AccountPage
from curl import *

class TestAccountPage:
    @allure.title("Проверка успешного перехода авторизованного пользователя на страницу профиля кликом по кнопке Личный кабинет в шапке приложения")
    @allure.description("На главной странице кликнуть по кнопке Личный кабинет, предварительно авторизовав пользователя, и проверить, что произошел переход на страницу профиля")
    def test_moving_to_profile_page_by_account_button(self, driver, generate_user):
        email, password = generate_user
        account_page = AccountPage(driver)
        account_page.user_authorization(email,password)
        account_page.click_account_button()
        current_url = account_page.get_current_url()
        assert current_url == Url.PROFILE_PAGE

    @allure.title("Проверка успешного перехода авторизованного пользователя в раздел История Заказов на страниц аккаунта кликом по кнопке История Заказов")
    @allure.description("На странице профиля кликнуть по кнопке История Заказов и проверить, что произошел переход в раздел истории заказов")
    def test_moving_to_order_history_section(self, driver, generate_user):
        email, password = generate_user
        account_page = AccountPage(driver)
        account_page.user_authorization(email, password)
        account_page.click_account_button()
        account_page.click_orders_history_button()
        current_url = account_page.get_current_url()
        assert current_url == Url.USER_ORDERS_PAGE

    @allure.title("Проверка успешного выхода авторизованного пользователя из аккаунта кликом по кнопке Выход")
    @allure.description("На странице профиля кликнуть по кнопке Выход и проверить, что произошел переход на страницу Авторизации")
    def test_moving_to_order_history_section(self, driver, generate_user):
        email, password = generate_user
        account_page = AccountPage(driver)
        account_page.user_authorization(email, password)
        account_page.click_account_button()
        account_page.click_exit_account_button()
        current_url = account_page.get_current_url()
        assert current_url == Url.LOGIN_PAGE
