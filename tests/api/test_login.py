import allure
import pytest
import requests

from data import const


class TestLogin:
    JIRA_URL = 'https://jira.hillel.it/rest/auth/1/session'

    @pytest.mark.api
    @pytest.mark.parametrize("login,password,status_code", [(const.USERNAME, const.PASSWORD, 200),
                                                            (const.USERNAME, "wrong pass", 401),
                                                            ("wrong username", const.PASSWORD, 401)])
    @allure.title("Login test")
    def test_login_with_wrong_password(self, login, password, status_code):
        auth_data = {
            "username": login,
            "password": password
        }
        print(auth_data)
        headers = {'Content-Type': 'application/json'}
        request = requests.post(self.JIRA_URL, json=auth_data, headers=headers)
        print(request.status_code)
        assert request.status_code == status_code

