import allure
import pytest

from data import const
from pages.jira_header import Header
from pages.login_page import LoginPage


@pytest.mark.usefixtures("get_driver")
class TestLogin:

    def setup(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.open()

    @pytest.mark.webtest
    @allure.title("Login with wrong password")
    def test_login_with_wrong_password(self):
        self.login_page.set_username(const.USERNAME)
        self.login_page.set_password("wrong pass")
        self.login_page.click_login()
        assert self.login_page.is_error_visible()

    @pytest.mark.webtest
    @allure.title("Login with wrong username")
    def test_login_with_wrong_username(self):
        self.login_page.set_username("wrong username")
        self.login_page.set_password(const.PASSWORD)
        self.login_page.click_login()
        assert self.login_page.is_error_visible()

    @pytest.mark.webtest
    @allure.title("Login test - positive")
    def test_login_positive(self):
        self.login_page.login(const.USERNAME, const.PASSWORD)
        assert Header(self.driver).is_profile_logo_visible()
