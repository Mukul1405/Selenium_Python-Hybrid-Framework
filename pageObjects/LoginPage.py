import selenium
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username = "//input[@placeholder='Username']"
    textbox_password = "//input[@placeholder='Password']"
    submit_btn = "//button[@type='submit']"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username).clear()
        self.driver.find_element(By.XPATH,self.textbox_username).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.textbox_password).clear()
        self.driver.find_element(By.XPATH,self.textbox_password).send_keys(password)

    def submitBtn(self):
        self.driver.find_element(By.XPATH,self.submit_btn).click()
