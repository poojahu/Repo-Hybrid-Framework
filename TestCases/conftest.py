import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture
def setup(browser):
    if browser == 'edge':
        options = Options()
        # Critical flags for Jenkins stability
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--headless=new")   # important in CI

        # Force a clean profile directory so Edge doesn't try to use SYSTEM defaults
        options.add_argument("--user-data-dir=C:\\Temp\\EdgeProfile")

        driver = webdriver.Edge(options=options)  # Selenium 4 auto-manages driver
        driver.maximize_window()
    elif browser=='chrome':
        opt=webdriver.ChromeOptions()
        opt.add_argument("--incognito")
        driver=webdriver.Chrome(options=opt)
        driver.maximize_window()
    else:
        opt=webdriver.ChromeOptions()
        opt.add_argument("--incognito")
        driver=webdriver.Chrome(options=opt)
        driver.maximize_window()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser") # this will get the value from cli/hooks

@pytest.fixture
def browser(request):
    browser=request.config.getoption("--browser") # this will return browser value to setup method
    return browser


# def pytest_configure(config):
#     config._metadata['Project Name']="OrangeHRM"
#     config._metadata['Tested By']="Pooja H U"
#
# @pytest.mark.optionalhook
# def pytestmetadata(metadata):
#     metadata.pop('Packages', None)
