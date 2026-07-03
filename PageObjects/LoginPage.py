from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    username_xpath="//input[@placeholder='Username']"
    password_xpath="//input[@placeholder='Password']"
    login_button_xpath="//button[@type='submit']"
    user_icon_xpath="//p[@class='oxd-userdropdown-name']"
    logout_option_xpath="//ul[@class='oxd-dropdown-menu']/li[4]"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.username_xpath)))
        self.driver.find_element(By.XPATH,self.username_xpath).clear()
        self.driver.find_element(By.XPATH,self.username_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH,self.password_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        WebDriverWait(self.driver, 8).until(EC.presence_of_element_located((By.XPATH, self.user_icon_xpath)))

    def click_usericon(self):
        self.driver.find_element(By.XPATH,self.user_icon_xpath).click()

    def click_logout(self):
        WebDriverWait(self.driver,2).until(EC.presence_of_element_located((By.XPATH,self.logout_option_xpath)))
        self.driver.find_element(By.XPATH,self.logout_option_xpath).click()
