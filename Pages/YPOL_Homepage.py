
import Locators.locators as l

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def ypol_search(self, phrase):
        self.driver.find_element_by_xpath(l.business_type_input).send_keys(phrase)
        self.driver.find_element_by_xpath(l.search_button).click()
