import allure
from pages.recover_passord_page import RecoveryPasswordPage
from curl import *

class TestRecoverPasswordPage:
    @allure.title("Проверка успешного перехода на страницу восстановления пароля кликом по кнопке Восстановить пароль на страницу авторизации пользователя")
    @allure.description("На странице авторизации пользователя кликаем по кнопке Восстановить пароль и проверяем, что загрузилась страница восстановления пароля")
    def test_moving_to_recover_password_page_by_recover_button(self, driver):
        recover_password_page = RecoveryPasswordPage(driver)
        recover_password_page.click_account_button()
        recover_password_page.click_recover_password_button()
        assert driver.current_url == Url.PASSWORD_RECOVERY_PAGE

    @allure.title("Проверка успешного ввода электронной почты в поле email и клика по кнопке Восстановить на странице восстановления пароля")
    @allure.description("На странице восстановления пароля вводим электронную почту пользователя в поле Email и кликаем по кнопке Восстановить, ожидая успешного перехода на экран смены пароля")
    def test_email_input_and_recover_button_click(self, driver, generate_user):
        email, password = generate_user
        recover_password_page = RecoveryPasswordPage(driver)
        recover_password_page.click_account_button()
        recover_password_page.click_recover_password_button()
        recover_password_page.insert_email(email)
        recover_password_page.click_button_recover()
        current_url = recover_password_page.get_current_url()
        assert current_url == Url.PASSWORD_RESET_PAGE

    @allure.title("Проверка поля Пароль на странице восстановления пароля на корректную работу подсветки поля при нажатии на кнопку в виде глаза, открывающую введенный в поле пароль")
    @allure.description("На странице ввода нового пароля нажимаем на кнопку в виде глаза и ожидаем, что поле пароля станет активным и выделится цветом ")
    def test_password_field_activation(self, driver, generate_user):
        email, password = generate_user
        recover_password_page = RecoveryPasswordPage(driver)
        recover_password_page.click_account_button()
        recover_password_page.click_recover_password_button()
        recover_password_page.insert_email(email)
        recover_password_page.click_button_recover()
        recover_password_page.click_show_password_button()
        assert recover_password_page.check_type_active_password_field() == "input pr-6 pl-6 input_type_text input_size_default input_status_active"
