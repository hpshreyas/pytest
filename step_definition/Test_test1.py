import pytest
from pytest_bdd import scenarios, given, then, parsers, when
from selenium import webdriver
import pytest_html
from selenium.webdriver.common.keys import Keys
import Constants.Utils as u
from Pages.YPOL_Homepage import HomePage
from Pages.YPOL_Resultspage import ResultsPage

# Scenarios
scenarios('../feature/Test1.feature')


# When Steps
@when(parsers.parse('the user searches for "{phrase}"'))
def search(browser, phrase):
    h = HomePage(browser)
    h.ypol_search(phrase)


# When Steps
@when(parsers.parse('the user clicks on "{phrase}" icon'))
@when(parsers.parse('the user clicks on "{phrase}" icon'))
def submit(browser, phrase):
    h = HomePage(browser)
    h.search_thumbs_container(phrase)


@when("user checks on now open")
def now_open(browser):
    h = HomePage(browser)
    h.check_now_open()


# Then Steps
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    r = ResultsPage(browser)
    r.ypol_search_results(phrase)


# Then Steps
@then("display the advertisers that are open now")
def display_outcome(browser):
    browser.implicitly_wait(10)
