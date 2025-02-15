import requests
from curl import Url

class AuthPage:

    @staticmethod
    def create_user(user_data):
        return requests.post(f'{Url.BASE_URL}{Url.USER_REGISTRATION_URL}', json=user_data)

    @staticmethod
    def delete_user(headers):
        return requests.delete(f"{Url.BASE_URL}{Url.USER_INFORMATION_URL}", headers=headers)