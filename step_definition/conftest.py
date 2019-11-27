import pytest

from pytest_bdd import given
from selenium import webdriver
import Constants.Utils as u

# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Shared Given Steps

@given('the YellowPages home page is displayed')
def launch_homepage(browser):
    browser.get(u.Homepage_url)
    browser.maximize_window()