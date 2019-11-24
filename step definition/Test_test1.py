import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import Constants.constants as c
from Pages.YPOL_Homepage import HomePage
from Pages.YPOL_Resultspage import ResultsPage



# Scenarios
scenarios('../feature/Test1.feature')


# Fixtures

@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    yield
    driver.close()
    driver.quit()


# Given Steps
@given('the YellowPages home page is displayed')
def launch_Homepage(test_setup):
    driver.get(c.Homepage_url)

# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search(test_setup, phrase):
    h = HomePage(driver)
    h.ypol_search(phrase)


# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(test_setup, phrase):
    r = ResultsPage(driver)
    r.ypol_search_results(phrase)
