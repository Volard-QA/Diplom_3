import pytest
import sys
import os
from selenium import webdriver

from generators import generate_new_user_data

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from curl import Url
from pages.auth_page import AuthPage

@pytest.fixture (params = ["chrome", "firefox"], scope='function')
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.get(Url.MAIN_SITE)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.get(Url.MAIN_SITE)
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def generate_user():
    login_pass = generate_new_user_data()
    user_data = {
        "email": login_pass['email'],
        "password": login_pass['password'],
        "name": login_pass['name']
    }
    response = AuthPage.create_user(user_data)
    response_data = response.json()
    email = user_data['email']
    password = user_data['password']
    yield email, password
    access_token = response_data['accessToken']
    headers = {'Authorization': access_token}
    AuthPage.delete_user(headers)
