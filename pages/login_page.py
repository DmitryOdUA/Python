import allure
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://jira.hillel.it"
    USERNAME_INPUT = (By.ID, "login-form-username")
    PASSWORD_INPUT = (By.ID, "login-form-password")
    ERROR_CONTAINER = (By.ID, "usernameerror")
    LOGIN_BUTTON = (By.ID, "login")

    def open(self):
        with allure.step("Open login page"):
            self.driver.get(self.URL)

    def login(self, username: str, password: str):
        with allure.step("Login with username: {} and password: {}".format(username, password)):
            self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
            self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
            self.driver.find_element(*self.LOGIN_BUTTON).click()
            WebDriverWait(self.driver, 5, 1, [TimeoutException]) \
                .until(EC.invisibility_of_element(self.LOGIN_BUTTON))

    def set_username(self, username: str):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def set_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_error_visible(self):
        return WebDriverWait(self.driver, 5, 1, [NoSuchElementException])\
            .until(EC.presence_of_element_located(self.ERROR_CONTAINER))\
            .is_displayed()
