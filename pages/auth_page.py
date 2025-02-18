import requests
from curl import Url
from pages.base_page import BasePage


class AuthPage(BasePage):

    @staticmethod
    def create_user(user_data):
        return requests.post(f'{Url.BASE_URL}{Url.USER_REGISTRATION_URL}', json=user_data)

    @staticmethod
    def delete_user(headers):
        return requests.delete(f"{Url.BASE_URL}{Url.USER_INFORMATION_URL}", headers=headers)
