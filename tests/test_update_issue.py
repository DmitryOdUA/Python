import random

import allure
import pytest

from data import const
from pages.create_issue_page import CreateIssuePage
from pages.issue_details_page import IssueDetailsPage
from pages.jira_header import Header
from pages.login_page import LoginPage
from pages.search_page import SearchPage


@pytest.mark.usefixtures("get_driver")
class TestSearchIssue:

    def setup(self):
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login(const.USERNAME, const.PASSWORD)
        self.header = Header(self.driver)
        self.header.click_create_button()
        create_issue_page = CreateIssuePage(self.driver)
        self.issue_summary = const.PREFIX + str(round(random.random() * 100000))
        create_issue_page.set_summary(self.issue_summary)
        create_issue_page.click_create_button()
        create_issue_page.wait_until_page_disappear()
        self.search_page = SearchPage(self.driver)
        self.issue_details_page = IssueDetailsPage(self.driver)

    @pytest.mark.webtest
    @allure.title("Update issue summary")
    def test_update_issue_summary(self):
        self.header.go_to_search_page()
        self.search_page.search_issue(self.issue_summary)
        self.search_page.select_issue(self.issue_summary)
        updated_summary = self.issue_summary + "UPDATED"
        self.issue_details_page.set_summary(updated_summary)
        assert self.issue_details_page.get_summary() == updated_summary

    @pytest.mark.webtest
    @allure.title("Update issue priority")
    def test_update_issue_priority(self):
        self.header.go_to_search_page()
        self.search_page.search_issue(self.issue_summary)
        self.search_page.select_issue(self.issue_summary)
        updated_priority = "High"
        self.issue_details_page.set_priority(updated_priority)
        assert self.issue_details_page.get_priority() == updated_priority

    @pytest.mark.webtest
    @allure.title("Update issue assignee")
    def test_update_issue_assignee(self):
        self.header.go_to_search_page()
        self.search_page.search_issue(self.issue_summary)
        self.search_page.select_issue(self.issue_summary)
        self.issue_details_page.set_assignee(const.USERNAME)
        assert self.issue_details_page.get_assignee() == const.USERNAME
