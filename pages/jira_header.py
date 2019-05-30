import time

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class Header(BasePage):
    PROFILE_LOGO = (By.ID, "header-details-user-fullname")
    CREATE_BUTTON = (By.ID, "create-menu")
    QUICK_SEARCH_INPUT = (By.ID, "quickSearchInput")
    ISSUES_BUTTON = (By.ID, "find_link")
    SEARCH_ISSUES_LINK = (By.ID, "issues_new_search_link_lnk")

    def is_profile_logo_visible(self):
        return WebDriverWait(self.driver, timeout=5, poll_frequency=1, ignored_exceptions=[NoSuchElementException])\
            .until(EC.presence_of_element_located(self.PROFILE_LOGO))\
            .is_displayed()

    def click_create_button(self):
        try:
            self.driver.find_element(*self.CREATE_BUTTON).click()
        except StaleElementReferenceException as Exception:
            print(Exception.msg)
            self.driver.find_element(*self.CREATE_BUTTON).click()

    def search(self, text: str):
        search_input = self.driver.find_element(*self.QUICK_SEARCH_INPUT)
        search_input.send_keys(text)
        search_input.find_element(By.PARTIAL_LINK_TEXT, text).click()

    def go_to_search_page(self):
        WebDriverWait(self.driver, timeout=5, poll_frequency=1, ignored_exceptions=[ElementClickInterceptedException]) \
            .until(EC.element_to_be_clickable(self.ISSUES_BUTTON)).click()
        # self.driver.find_element(*self.ISSUES_BUTTON).click()
        self.driver.find_element(*self.SEARCH_ISSUES_LINK).click()

