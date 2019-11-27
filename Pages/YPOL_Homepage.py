
import Locators.locators as l

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def ypol_search(self, phrase):
        self.driver.find_element_by_xpath(l.business_type_input).send_keys(phrase)
        self.driver.find_element_by_xpath(l.search_button).click()

    def search_thumbs_container(self, phrase):
        self.driver.find_element_by_xpath(l.bullet_lawyers).click()

    def search_nowOpen_ad(self):
        self.driver.find_element_by_xpath(l.now_open).click()

    def check_now_open(self):
        validate = self.driver.find_element_by_xpath(l.now_open)
        validate.click()
