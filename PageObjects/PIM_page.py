from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIM_Page:
    pim_option_xpath="//span[text()='PIM']"
    pim_header_xpath="//span[@class='oxd-topbar-header-breadcrumb']"
    add_emp_xpath="//a[text()='Add Employee']"
    add_emp_form_xpath="//div[@class='orangehrm-card-container']"

    emp_first_name_xpath="//input[@name='firstName' and @placeholder='First Name']"
    emp_mid_name_xpath="//input[@name='middleName' and @placeholder='Middle Name']"
    emp_last_name_xpath="//input[@name='lastName' and @placeholder='Last Name']"
    emp_id_xpath="//div[@class='oxd-grid-2 orangehrm-full-width-grid']//input"

    create_login_checkbox_xpath="//div[@class='oxd-switch-wrapper']//input[@type='checkbox']"
    cancel_button_xpath="//div[@class='oxd-form-actions']//button[1]"
    save_button_xpath="//div[@class='oxd-form-actions']//button[2]"

    emp_username_xpath="//div[@class='orangehrm-employee-form']/div[3]//div[2]/input"
    status_enabled_xpath="//input[@type='radio' and @value='1']"
    status_disabled_xpath="//input[@type='radio' and @value='2']"
    emp_password_xpath="//div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']//input[@type='password']"
    emp_confirm_password_xpath="//div[@class='oxd-grid-item oxd-grid-item--gutters']//input[@type='password']"

    pim_add_emp_form_error_xpath="//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
    pim_emp_edit_form_xpath="//div[@class='orangehrm-edit-employee']"

    def __init__(self,driver):
        self.driver = driver

    def clickPIM(self):
        #WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,self.pim_option_xpath)))
        self.driver.find_element(By.XPATH,self.pim_option_xpath).click()
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.XPATH,self.add_emp_xpath)))

    def clickAddEmployee(self):
        self.driver.find_element(By.XPATH,self.add_emp_xpath).click()
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.XPATH,self.add_emp_form_xpath)))

    def fillEmpName(self,firstname,middlename="",lastname=""):
        self.driver.find_element(By.XPATH,self.emp_first_name_xpath).clear()
        self.driver.find_element(By.XPATH,self.emp_first_name_xpath).send_keys(firstname)

        self.driver.find_element(By.XPATH,self.emp_mid_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.emp_mid_name_xpath).send_keys(middlename)

        self.driver.find_element(By.XPATH, self.emp_last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.emp_last_name_xpath).send_keys(lastname)

    def fillEmpId(self,empid):
        self.driver.find_element(By.XPATH,self.emp_id_xpath).click()
        act=ActionChains(self.driver)
        act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).key_down(Keys.DELETE).perform()
        self.driver.find_element(By.XPATH,self.emp_id_xpath).send_keys(empid)

    def clickCreateLoginDetails(self):
        #self.driver.find_element(By.XPATH,self.create_login_checkbox_xpath).click()
        self.driver.execute_script("arguments[0].click();",(self.driver.find_element(By.XPATH,self.create_login_checkbox_xpath)))
        WebDriverWait(self.driver,3).until(EC.visibility_of_element_located((By.XPATH,self.emp_username_xpath)))

    def fillEmpUsername(self,username):
        self.driver.find_element(By.XPATH,self.emp_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.emp_username_xpath).send_keys(username)

    def statusRadioButtonSelect(self):
        enabled=self.driver.find_element(By.XPATH,self.status_enabled_xpath)
        disabled=self.driver.find_element(By.XPATH,self.status_disabled_xpath)
        if enabled.is_selected():
            pass
        else:
            enabled.click()

    def fillPassword(self,password):
        self.driver.find_element(By.XPATH,self.emp_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.emp_password_xpath).send_keys(password)
        self.driver.find_element(By.XPATH, self.emp_confirm_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.emp_confirm_password_xpath).send_keys(password)

    def clickSave(self):
        self.driver.find_element(By.XPATH,self.save_button_xpath).click()
        #WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH,self.pim_emp_edit_form_xpath)))

    def clickCancel(self):
        self.driver.find_element(By.XPATH,self.cancel_button_xpath).click()

    def get_errors(self):
        errors=self.driver.find_elements(By.XPATH,self.pim_add_emp_form_error_xpath)
        print(len(errors))
        if len(errors)>=1:
            for er in errors:
                print(er.text)
        else:
            print("****************** No errors in Add Employee form all fields are filled correctly ***************")
