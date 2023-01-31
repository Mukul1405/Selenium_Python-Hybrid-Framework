import time

import selenium
import sys
sys.path.append("..")
from pageObjects.LoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    print(baseurl,username,password)

    logger = LogGen.loggen()

    def test_homePagetitle(self,setup):
        self.logger.info("**************** TEST01 Login ***************")
        self.logger.info("**************** Verify HomePage Title ***************")
        self.driver = setup
        print(self.baseurl)
        self.driver.get(str(self.baseurl))
        title = self.driver.title
        if title == "OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("**************** Home Page Title test is passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homePagetitle.png")
            self.driver.close()
            self.logger.error("**************** Home Page Title test is failed ***************")
            assert False


    # def test_login(self,setup):
    #     self.logger.info("**************** Login Test Case Started ***************")
    #     self.driver = setup
    #     self.driver.get(self.baseurl)
    #     login = LoginPage(self.driver)
    #     time.sleep(5)
    #     login.setUsername(username=self.username)
    #     login.setPassword(password=self.password)
    #     login.submitBtn()
    #
    #     WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.TAG_NAME,"h6")))
    #     if self.driver.find_element(By.TAG_NAME, "h6").text == "Dashboard":
    #         assert True
    #         self.logger.info("**************** Login test is passed ***************")
    #         self.driver.close()
    #     else:
    #         self.driver.close()
    #         self.logger.error("**************** Login test is passed ***************")
    #         assert False




