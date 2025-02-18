from selenium.webdriver.common.by import By

class RecoverPasswordPageLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@class="text input__textfield text_type_main-default" and @name="name"]')
    RECOVER_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')
    HIDE_PASSWORD_BUTTON = (By.XPATH, '//div[@class="input pr-6 pl-6 input_type_password input_size_default"]//div[@class="input__icon input__icon-action"]')
    PASSWORD_FIELD_ACTIVE = (By.XPATH, '//div[@class="input__container"]//div[@class="input pr-6 pl-6 input_type_text input_size_default input_status_active"]')
    SAVE_PASSWORD_BUTTON = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa"]')