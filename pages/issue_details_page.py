from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class IssueDetailsPage(BasePage):
    EDIT_BUTTON = (By.ID, "edit-issue")
    SUMMARY_VALUE = (By.ID, "summary-val")
    SUMMARY_INPUT = (By.ID, "summary")
    ASSIGNEE_VALUE = (By.ID, "assignee-val")
    ASSIGNEE_INPUT = (By.ID, "assignee-field")
    PRIORITY_VALUE = (By.ID, "priority-val")
    PRIORITY_INPUT = (By.ID, "priority-field")
    LOADING_INDICATOR = (By.CLASS_NAME, "loading")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    def click_edit_button(self):
        self.driver.find_element(*self.EDIT_BUTTON).click()

    def get_summary(self):
        return self.driver.find_element(*self.SUMMARY_VALUE).text

    def set_summary(self, summary: str):
        try:
            self.driver.find_element(*self.SUMMARY_VALUE).click()
        except StaleElementReferenceException as Exception:
            self.driver.find_element(*self.SUMMARY_VALUE).click()
        self.driver.find_element(*self.SUMMARY_INPUT).send_keys(summary + "\n")
        WebDriverWait(self.driver, timeout=5, poll_frequency=1) \
            .until(EC.text_to_be_present_in_element(self.SUMMARY_VALUE, summary))

    def get_priority(self):
        return self.driver.find_element(*self.PRIORITY_VALUE).text

    def set_priority(self, priority: str):
        WebDriverWait(self.driver, timeout=5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]) \
            .until(EC.invisibility_of_element(self.LOADING_INDICATOR))
        self.driver.find_element(*self.PRIORITY_VALUE).click()
        self.driver.find_element(*self.PRIORITY_INPUT).send_keys(priority + "\n")
        self.driver.find_element(*self.PRIORITY_VALUE).find_element(*self.SUBMIT_BUTTON).click()
        WebDriverWait(self.driver, timeout=5, poll_frequency=1) \
            .until(EC.text_to_be_present_in_element(self.PRIORITY_VALUE, priority))

    def get_assignee(self):
        return self.driver.find_element(*self.ASSIGNEE_VALUE).text

    def set_assignee(self, assignee: str):
        WebDriverWait(self.driver, timeout=5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]) \
            .until(EC.invisibility_of_element(self.LOADING_INDICATOR))
        self.driver.find_element(*self.ASSIGNEE_VALUE).click()
        self.driver.find_element(*self.ASSIGNEE_INPUT).send_keys(assignee + "\n")
        WebDriverWait(self.driver, timeout=5, poll_frequency=1) \
            .until(EC.text_to_be_present_in_element(self.ASSIGNEE_VALUE, assignee))
