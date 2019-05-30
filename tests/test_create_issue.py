import random
import string

import pytest
import allure

from data import const
from pages.create_issue_page import CreateIssuePage
from pages.jira_header import Header
from pages.login_page import LoginPage
from pages.notifications import Notifications


@pytest.mark.usefixtures("get_driver")
class TestCreateIssue:

    def setup(self):
        self.header = Header(self.driver)
        self.create_issue_page = CreateIssuePage(self.driver)
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(const.USERNAME, const.PASSWORD)

    @pytest.mark.skip
    @pytest.mark.webtest
    @allure.title("Create issue test - positive")
    def test_create_issue_positive(self):
        self.header.click_create_button()
        self.create_issue_page.set_summary(const.PREFIX + str(round(random.random() * 100000)))
        self.create_issue_page.click_create_button()
        assert Notifications(self.driver).is_issue_created_popup_displayed()

    @pytest.mark.webtest
    @allure.title("Create issue with empty summary")
    def test_create_issue_with_missing_summary(self):
        self.header.click_create_button()
        self.create_issue_page.click_create_button()
        assert self.create_issue_page.is_error_with_text_visible("You must specify a summary of the issue.")

    @pytest.mark.webtest
    @allure.title("Create issue too long summary")
    def test_create_issue_long_summary(self):
        self.header.click_create_button()
        long_summary = ''.join(random.choice(string.ascii_lowercase) for x in range(256))
        self.create_issue_page.set_summary(long_summary)
        self.create_issue_page.click_create_button()
        assert self.create_issue_page.is_error_with_text_visible("Summary must be less than 255 characters.")