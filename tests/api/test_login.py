import allure
import pytest
import requests

from data import const


class TestLogin:
    JIRA_URL = 'https://jira.hillel.it/rest/auth/1/session'
    RERUN_PASSWORD_LIST = ["dsfdfd", const.PASSWORD]

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
        headers = {'Content-Type': 'application/json'}
        request = requests.post(self.JIRA_URL, json=auth_data, headers=headers)
        assert request.status_code == status_code

    @pytest.mark.api
    @allure.title("Rerun - flaky login test")
    def test_login_with_rerun(self):
        auth_data = {
            "username": const.USERNAME,
            "password": self.RERUN_PASSWORD_LIST.pop(0)
        }
        headers = {'Content-Type': 'application/json'}
        request = requests.post(self.JIRA_URL, json=auth_data, headers=headers)
        assert request.status_code == 200

