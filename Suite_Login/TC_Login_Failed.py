import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Test_Login_failed(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_Login_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") #open browser
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("Aji bay") #INPUT USERNAME
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin123") #INPUT password
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click() #button login
        time.sleep(2)                                   
       


    def test_b_Login_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("tes123")
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(2)                                   
       

    def test_c_Login_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin22")
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin1234")
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(2)                                   
        
    def test_d_Login_failed(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(2)
        driver.find_element(By.NAME, "username").send_keys("")
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()
        time.sleep(2)                                   
       

    def tearDown(self): 
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()