import random
import string

import allure
import pytest
import requests
from requests.auth import HTTPBasicAuth

from data import const, fixtures


class TestCreateIssue:
    ISSUES_ENDPOINT = const.JIRA_URL + '/rest/api/2/issue'
    EMPTY_SUMMARY_ERROR = "You must specify a summary of the issue."
    LONG_SUMMARY_ERROR = "Summary must be less than 255 characters."
    issue_id: str = None

    @pytest.mark.api
    @allure.title("Login test")
    def test_create_issue_positive(self):
        issue_json = fixtures.get_issue_json(const.PREFIX + str(round(random.random() * 100000)))
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.ISSUES_ENDPOINT, json=issue_json, headers=headers,
                                 auth=HTTPBasicAuth(const.USERNAME, const.PASSWORD))
        self.issue_id = response.json().get("id", None)
        assert 201 == response.status_code

    @pytest.mark.api
    @pytest.mark.parametrize("summary,status_code,error_message",
                             [("", 400, EMPTY_SUMMARY_ERROR),
                              (const.PREFIX.join(random.choice(string.ascii_lowercase) for x in range(256)), 400, LONG_SUMMARY_ERROR)])
    @allure.title("Login test")
    def test_create_issue_negative(self, summary, status_code, error_message):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.ISSUES_ENDPOINT, json=fixtures.get_issue_json(summary), headers=headers,
                                 auth=HTTPBasicAuth(const.USERNAME, const.PASSWORD))
        assert status_code == response.status_code
        assert error_message == response.json()["errors"]["summary"]

    def teardown_method(self):
        if self.issue_id is not None:
            headers = {'Content-Type': 'application/json'}
            requests.delete(self.ISSUES_ENDPOINT + "/" + self.issue_id, headers=headers,
                            auth=HTTPBasicAuth(const.USERNAME, const.PASSWORD))
