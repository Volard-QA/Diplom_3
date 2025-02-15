from selenium.webdriver.common.by import By

class OrdersListLocators:
    ORDER_IN_LIST = (By.XPATH, '//ul[@class="OrderFeed_list__OLh59"]//li[@class="OrderHistory_listItem__2x95r mb-6"]')
    ORDER_DESCRIPTION_WINDOW = (By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]//p[@class="text text_type_main-medium mb-8"]')
    ORDER_NUMBER_IN_ORDER_LIST_WINDOW = (By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]//p[@class="text text_type_digits-default mb-10 mt-5"]')
    ORDER_IN_ORDER_HISTORY_WINDOW = (By.XPATH, '//div[@class="OrderHistory_orderHistory__qy1VB"]//li[@class="OrderHistory_listItem__2x95r mb-6"][last()]')
    ORDER_NUMBER_IN_ORDER_HISTORY_WINDOW = (By.XPATH, '//div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]//p[@class="text text_type_digits-default mb-10 mt-5"]')
    NUMBER_IN_ALL_ORDERS_COUNTER = (By.XPATH, '//div[@class="undefined mb-15"]//p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]')
    NUMBER_IN_TODAY_ORDERS_COUNTER = (By.XPATH, '(//p[contains(@class, "OrderFeed_number__2MbrQ text text_type_digits-large")])[2]')
    NUMBER_IN_PREPARING_ORDERS = (By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]//li[@class="text text_type_digits-default mb-2"]')
    ORDER_NUMBER_IN_ORDER_CREATION_WINDOW = (By.XPATH, '//div[@class="Modal_modal__contentBox__sCy8X pt-30 pb-30"]//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
