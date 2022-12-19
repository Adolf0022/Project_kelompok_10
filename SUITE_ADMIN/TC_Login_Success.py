import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

#LOGIN SUCCESSFULLY
class Test_Login(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_Login_successfully(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") #OPEN BROWSER
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin") #INPUT USERNAME
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin123") #INPUT PASSWORD
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click() #CLICK BUTTON LOGIN
        time.sleep(2)                                   
        Dashboard_tag = driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']/span[.='Dashboard']" ) #VIEW DASHBOARD
        self.assertEqual(Dashboard_tag.text, "Dashboard")  
        time.sleep(2)

    def tearDown(self): 
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()