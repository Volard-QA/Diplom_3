import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.account_locators import AccountPageLocators
from locators.login_page_locators import LoginPageLocators

class AccountPage(BasePage):

    @allure.step("Авторизация пользователя")
    def user_authorization(self, email, password):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ACCOUNT_BUTTON)
        self.wait_for_login_page_load()
        self.click_on_element(LoginPageLocators.EMAIL_FIELD)
        self.insert_keys_into_input(LoginPageLocators.EMAIL_FIELD_ACTIVE, email)
        self.click_on_element(LoginPageLocators.PASSWORD_FIELD)
        self.insert_keys_into_input(LoginPageLocators.PASSWORD_FIELD_ACTIVE, password)
        self.click_on_element(LoginPageLocators.ENTER_BUTTON)

    @allure.step("Клик по кнопке Личный кабинет на главной странице")
    def click_account_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ACCOUNT_BUTTON)
        self.wait_for_profile_page_load()

    @allure.step("Клик по кнопке История заказов на странице профиля пользователя")
    def click_orders_history_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ORDERS_HISTORY_BUTTON)
        self.wait_for_order_history_page_load()

    @allure.step("Клик по кнопке Выход на странице профиля пользователя")
    def click_exit_account_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(AccountPageLocators.EXIT_ACCOUNT_BUTTON)
        self.wait_for_login_page_load()

