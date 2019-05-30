from enum import Enum

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CreateIssuePage(BasePage):
    SUMMARY_INPUT = (By.ID, "summary")
    PRIORITY_INPUT = (By.ID, "priority-field")
    ASSIGNEE_INPUT = (By.ID, "assignee-field")
    CREATE_BUTTON = (By.ID, "create-issue-submit")
    ERROR_TEXT = (By.CLASS_NAME, "error")

    def set_summary(self, summary: str):
        self.driver.find_element(*self.SUMMARY_INPUT).send_keys(summary)

    def set_priority(self, priority: str):
        self.driver.find_element(*self.PRIORITY_INPUT).send_keys(priority + "\n")

    def set_assignee(self, assignee: str):
        self.driver.find_element(*self.ASSIGNEE_INPUT).send_keys(assignee + "\n")

    def click_create_button(self):
        self.driver.find_element(*self.CREATE_BUTTON).click()

    def is_error_with_text_visible(self, error_text: str):
        errors = self.driver.find_elements(*self.ERROR_TEXT)
        for error in errors:
            if error.text == error_text:
                return True
        return False

    def wait_until_page_disappear(self):
        return WebDriverWait(self.driver, timeout=5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]) \
            .until(EC.invisibility_of_element(self.CREATE_BUTTON))