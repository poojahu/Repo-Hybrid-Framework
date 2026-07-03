import time

import pytest

from PageObjects.LoginPage import LoginPage
from Utilities.customlogger import LogGenerator
from Utilities.readproperty import ReadConfig


class TestLogin:
    url=ReadConfig.get_url()
    username=ReadConfig.get_username()
    password=ReadConfig.get_password()
    logger=LogGenerator.logs_gen()

    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        obj_login=LoginPage(self.driver)
        self.logger.info("**************************Test Case: Test Login page********************")
        obj_login.set_username(self.username)
        obj_login.set_password(self.password)
        obj_login.click_login()
        self.logger.info("**************************Trying to login with username and password**********************")
        if "dashboard" in self.driver.current_url:
            self.logger.info("**************************login successful********************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png") #.\\ represents current project
            self.logger.info("**************************Login Failed********************")
            assert False
        self.driver.close()

    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_logout(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        obj_login=LoginPage(self.driver)
        self.logger.info("**************************Test case: Test logout**********************")
        obj_login.set_username(self.username)
        obj_login.set_password(self.password)
        obj_login.click_login()
        self.logger.info("**************************Logging in with valid username and password**********************")
        obj_login.click_usericon()
        obj_login.click_logout()
        self.logger.info("**************************Clicked Log Out*********************")
        time.sleep(2)
        assert "login" in self.driver.current_url
        self.logger.info("**************************Logged out Successfully**********************")
        self.driver.close()


