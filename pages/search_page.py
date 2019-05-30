import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class SearchPage(BasePage):
    ISSUE_SUMMARY = (By.CLASS_NAME, "issue-link-summary")
    SEARCH_QUERY_INPUT = (By.ID, "searcher-query")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Search']")
    EDIT_BUTTON = (By.ID, "opsbar-edit-issue_container")
    LOADING_INDICATOR = (By.CLASS_NAME, "loading")

    def is_issue_exist(self, summary: str):
        time.sleep(1)
        issues = self.driver.find_elements(*self.ISSUE_SUMMARY)
        for issue in issues:
            if issue.text == summary:
                return True
        return False

    def input_search_query(self, query: str):
        self.driver.find_element(*self.SEARCH_QUERY_INPUT).send_keys(query)

    def click_search_button(self):
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def search_issue(self, query: str):
        self.input_search_query(query)
        self.click_search_button()
        WebDriverWait(self.driver, timeout=5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]) \
            .until(EC.invisibility_of_element(self.LOADING_INDICATOR))

    def select_issue(self, summary: str):
        issues = self.driver.find_elements(*self.ISSUE_SUMMARY)
        for issue in issues:
            if issue.text == summary:
                try:
                    issue.click()
                except StaleElementReferenceException as Exception:
                    print(Exception.msg)
                    issue.click()

    def edit_issue(self, summary: str):
        time.sleep(4)
        issues = self.driver.find_elements(*self.ISSUE_SUMMARY)
        for issue in issues:
            if issue.text == summary:
                issue.click()
        try:
            self.driver.find_element(*self.EDIT_BUTTON).click()
        except StaleElementReferenceException as Exception:
            self.driver.find_element(*self.EDIT_BUTTON).click()