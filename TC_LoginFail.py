import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestLoginFailOrangeHRM(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_login_OrangeHRM_fail(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") #open Website 
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin") #input username
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin12345") #input password 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #click button Login 
        time.sleep(2)
        login_fail_text = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]") #validate error text 
        self.assertEqual(login_fail_text.text, "Invalid credentials")  
        time.sleep(2)
        
        print("Login Fail")
    
    def tearDown(self): 
        self.driver.close()
    
if __name__ == "__main__":
    unittest.main()