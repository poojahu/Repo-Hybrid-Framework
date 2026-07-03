import pytest
from selenium import webdriver

@pytest.fixture
def setup(browser):
    if browser=='edge':
        driver=webdriver.Edge(service=Service("C:\Users\pooja\.cache\selenium\msedgedriver\win64\150.0.4078.48\msedgedriver.exe"))
        driver.maximize_window()
    elif browser=='chrome':
        driver=webdriver.Chrome()
        driver.maximize_window()
    else:
        driver = webdriver.Chrome()
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
