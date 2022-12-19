import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Test_delete_admin_FAILED(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_delete_admin (self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(1)
        driver.find_element(By.NAME, "username").send_keys("Admin") #LOGIN USERNAME
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin123") #LOGIN PASSWORD
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click() #CLICK LOGIN 
        time.sleep(2)  
        driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']/span[.='Dashboard']" ) #OPEN DASBOARD
        time.sleep(2)    
        driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']" ).click() #VIEW ADMIN
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[13]/div/div[6]/div/button[1]' ).click()
        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[1]' ).click()
        time.sleep(5)
        
    def tearDown(self): 
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()