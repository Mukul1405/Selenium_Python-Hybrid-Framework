import time

import selenium
import sys
sys.path.append("..")
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_001_Login:
    baseurl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_homePagetitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        title = self.driver.title
        time.sleep(2)
        if title == "OrangeHRM":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePagetitle.png")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        login = LoginPage(self.driver)
        time.sleep(5)
        login.setUsername(username=self.username)
        time.sleep(1)
        login.setPassword(password=self.password)
        time.sleep(1)
        login.submitBtn()

        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h6")))
        if self.driver.find_element(By.TAG_NAME, "h6").text == "Dashboard":
            self.driver.close()
            assert True
        else:
            self.driver.close()
            assert False




