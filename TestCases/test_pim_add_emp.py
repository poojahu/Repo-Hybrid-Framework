import string
import random

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utilities.readproperty import ReadConfig
from PageObjects.LoginPage import LoginPage
from PageObjects.PIM_page import PIM_Page
from Utilities.customlogger import LogGenerator
import time

class TestPimAddEmp:
    log=LogGenerator.logs_gen()
    url=ReadConfig.get_url()
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()

    # emp_firstname=ReadConfig.get_emp_firstname()
    # emp_lastname=ReadConfig.get_emp_lastname()
    # emp_id=ReadConfig.get_emp_id()
    def generate_random_firstname(self, size=8, chars=string.ascii_lowercase + string.digits):
        emp_firstname = ''.join(random.choice(chars) for c in range(size))
        return emp_firstname

    def generate_random_lastname(self, size=5, chars=string.ascii_lowercase + string.digits):
        emp_lastname = ''.join(random.choice(chars) for c in range(size))
        return emp_lastname

    def generate_random_empid(self, size=3, chars=string.digits):
        emp_id = ''.join(random.choice(chars) for c in range(size))
        return emp_id

    emp_username=ReadConfig.get_emp_user()
    emp_password=ReadConfig.get_emp_pass()

    @pytest.mark.regression
    def test_pim_add_emp(self,setup):
        self.log.info("********************** Test PIM add Emp Testcase ******************************")
        self.driver = setup
        self.objLogin=LoginPage(self.driver)
        self.log.info("********************* Opening the URL *******************")
        self.driver.get(self.url)
        self.objLogin.set_username(self.username)
        self.objLogin.set_password(self.password)
        self.log.info("********************* Logging in with Credentials *******************")
        self.objLogin.click_login()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.objLogin.user_icon_xpath)))
        assert "dashboard" in self.driver.current_url

        self.log.info("********************* Going to PIM page *******************")
        self.objPIM=PIM_Page(self.driver)
        self.objPIM.clickPIM()
        self.objPIM.clickAddEmployee()

        self.log.info("********************* Adding employee details *******************")
        self.objPIM.fillEmpName(self.generate_random_firstname(), lastname=self.generate_random_lastname())
        self.objPIM.fillEmpId(self.generate_random_empid())
        self.objPIM.clickCreateLoginDetails()

        self.log.info("********************* Adding username and password for Employee *******************")
        self.objPIM.fillEmpUsername(self.emp_username)
        self.objPIM.statusRadioButtonSelect()
        self.objPIM.fillPassword(self.emp_password)
        time.sleep(2)

        self.objPIM.clickSave()
        self.objPIM.get_errors()
        self.log.info("********************* Saving details entered for Empolyee *******************")
        time.sleep(5)
        self.objLogin.click_usericon()
        self.objLogin.click_logout()

