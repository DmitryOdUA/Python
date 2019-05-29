import random

import allure
import pytest

from data import const
from pages.create_issue_page import CreateIssuePage
from pages.jira_header import Header
from pages.login_page import LoginPage
from pages.search_page import SearchPage


@pytest.mark.usefixtures("get_driver")
class TestSearchIssue:
    SUMMARY_PREFIX = "(PYTHON AUTOTEST)"

    def setup(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(const.USERNAME, const.PASSWORD)
        self.header = Header(self.driver)
        self.header.click_create_button()
        self.issue_summary = self.SUMMARY_PREFIX + str(round(random.random() * 100000))
        create_issue_page = CreateIssuePage(self.driver)
        create_issue_page.set_summary(self.issue_summary)
        create_issue_page.click_create_button()
        create_issue_page.wait_until_page_disappear()
        self.search_page = SearchPage(self.driver)

    @pytest.mark.skip
    @pytest.mark.webtest
    @allure.title("Search issue by summary")
    def test_search_issue_positive(self):
        self.header.go_to_search_page()
        self.search_page.input_search_query(self.issue_summary)
        self.search_page.click_search_button()
        assert self.search_page.is_issue_exist(self.issue_summary)

    @pytest.mark.skip
    @pytest.mark.webtest
    @allure.title("Search non existing issue")
    def test_search_issue_negative(self):
        self.header.go_to_search_page()
        self.search_page.input_search_query("This issue definitely should not exist!")
        self.search_page.click_search_button()
        assert not self.search_page.is_issue_exist(self.issue_summary)
