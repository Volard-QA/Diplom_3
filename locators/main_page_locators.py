from selenium.webdriver.common.by import By

class MainPageLocators:
    INGREDIENT_LOCATOR = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8')])")
    INGREDIENT_DESCRIPTION_TITLE = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]//h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]')
    CONSTRUCTOR_TITLE_TEXT = (By.XPATH, '//section[@class="BurgerIngredients_ingredients__1N8v2"]//h1[@class="text text_type_main-large mb-5 mt-10"]')
    COUNTER = (By.XPATH, '//a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8" and @href="/ingredient/61c0c5a71d1f82001bdaaa72"]//p[@class="counter_counter__num__3nue1"]')
    ORDER_WINDOW_TEXT = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]//p[@class="undefined text text_type_main-medium mb-15"]')