import time

import pytest

from PageObjects.LoginPage import LoginPage
from Utilities.customlogger import LogGenerator
from Utilities.readproperty import ReadConfig
from Utilities import excelutils


class TestLogin:
    url=ReadConfig.get_url()
    logger=LogGenerator.logs_gen()
    file=ReadConfig.get_file()
    sheetname=ReadConfig.get_sheetname()

    @pytest.mark.regression
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.url)
        obj_login=LoginPage(self.driver)
        self.logger.info("**************************Test Case: Test Login page for DDT ********************")
        rows=excelutils.get_rowcount(self.file,self.sheetname)
        list_actual=[]
        for row in range(2,rows+1):
            self.username=excelutils.read_data(self.file,self.sheetname,row,1)
            self.password=excelutils.read_data(self.file,self.sheetname,row,2)
            self.expected=excelutils.read_data(self.file,self.sheetname,row,3)

            obj_login.set_username(self.username)
            obj_login.set_password(self.password)
            obj_login.click_login()
            self.logger.info("**************************Trying login with username and password from excel sheet **********************")
            time.sleep(3)
            if "dashboard" in self.driver.current_url:
                if self.expected=="Pass":
                    list_actual.append("Passed")
                    obj_login.click_usericon()
                    obj_login.click_logout()
                    excelutils.write_data(self.file,self.sheetname,row,4,"Passed")

                elif self.expected=="Fail":
                    list_actual.append("Failed")
                    obj_login.click_usericon()
                    obj_login.click_logout()
                    excelutils.write_data(self.file,self.sheetname,row,4,"Failed")
            elif "dashboard" not in self.driver.current_url:
                if self.expected=="Fail":
                    list_actual.append("Passed")
                    excelutils.write_data(self.file, self.sheetname, row, 4, "Passed")
                elif self.expected=="Pass":
                    list_actual.append("Failed")
                    excelutils.write_data(self.file, self.sheetname, row, 4, "Failed")

        if "Failed" in list_actual:
            self.logger.info("*********************** Test Login DDT Failed ***********************")
            assert False
        else:
            self.logger.info("********************** Test Login DDT Passed **************************")
            assert True
        self.driver.close()
        self.logger.info("********************** End of Test login DDT *****************************")




