from selenium.webdriver.remote import webdriver


class BasePage(object):
    def __init__(self, driver):
        self.driver: webdriver.WebDriver = driver
