import allure

from pages.base_page import BasePage
from locators.recover_password_page_locators import RecoverPasswordPageLocators
from locators.base_page_locators import BasePageLocators
from locators.login_page_locators import LoginPageLocators

class RecoveryPasswordPage(BasePage):
    @allure.step("Клик по кнопке Личный кабинет на главной странице")
    def click_account_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(BasePageLocators.ACCOUNT_BUTTON)

    @allure.step("Клик по кнопке Восстановить пароль на странице авторизации")
    def click_recover_password_button(self):
        self.scroll_to_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)
        self.click_on_element(LoginPageLocators.RECOVER_PASSWORD_BUTTON)
        self.wait_for_recover_page_load()

    @allure.step("Заполнение поля Email на странице восстановления пароля")
    def insert_email(self, email):
        self.insert_keys_into_input(RecoverPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step("Клик по кнопке Восстановить на странице восстановления пароля")
    def click_button_recover(self):
        self.click_on_element(RecoverPasswordPageLocators.RECOVER_BUTTON)
        self.wait_for_reset_page_load()

    @allure.step("Клик по кнопке в виде глаза в поле пароль на странице замены пароля")
    def click_show_password_button(self):
        self.wait_for_element_to_hide(BasePageLocators.OVERLAY)
        self.click_on_element(RecoverPasswordPageLocators.HIDE_PASSWORD_BUTTON)

    @allure.step("Проверить, что атрибут type поля Пароль изменился на text")
    def check_type_active_password_field(self):
        password_field = self.wait_element(RecoverPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
        return password_field.get_attribute("class")

