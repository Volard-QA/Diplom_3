from selenium.webdriver.common.by import By

class BasePageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "(//a[contains(@class, 'AppHeader_header__link__3D_hX')])[3]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    ORDERS_LIST_LINK = (By.XPATH, "(//a[contains(@class, 'AppHeader_header__link__3D_hX')])[2]")
    SAUCE = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"]//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href="/ingredient/61c0c5a71d1f82001bdaaa72"]')
    BASKET = (By.XPATH, '//section[@class="BurgerConstructor_basket__29Cd7 mt-25 "]//ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    BREAD = (By.XPATH, '//ul[@class="BurgerIngredients_ingredients__list__2A-mT"]//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    DESCRIPTION_CLOSE_BUTTON = (By.XPATH, '//section[contains(@class, "Modal_modal_opened__3ISw4")]//button[contains(@class, "Modal_modal__close_modified__3V5XS")]')
    ORDERS_HISTORY_BUTTON = (By.XPATH, "(//a[contains(@class, 'Account_link__2ETsJ text text_type_main-medium text_color_inactive')])[2]")
    CONSTRUCTOR_LINK = (By.XPATH, "(//a[contains(@class, 'AppHeader_header__link__3D_hX')])")
