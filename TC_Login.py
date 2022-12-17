import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestLoginOrangeHRM(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_login_OrangeHRM_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)
        Dashboard_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span" )
        self.assertEqual(Dashboard_tag.text, "Dashboard")  
        time.sleep(2)
    
    def tearDown(self): 
        self.driver.close()
        
    def run(self):
        unittest.main()
if __name__ == "__main__":
    unittest.main()