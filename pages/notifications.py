from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Notifications(BasePage):
    ISSUE_CREATED_NOTIFICATION = (By.XPATH, "//div[@id='aui-flag-container']//a[contains(@class, 'issue-created-key')]")

    def is_issue_created_popup_displayed(self):
        return WebDriverWait(self.driver, timeout=5, poll_frequency=1, ignored_exceptions=[NoSuchElementException]) \
            .until(EC.visibility_of_element_located(self.ISSUE_CREATED_NOTIFICATION)) \
            .is_displayed()