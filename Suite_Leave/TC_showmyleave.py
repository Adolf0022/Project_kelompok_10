import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import TC_Login

class TestShowMyLeave(unittest.TestCase):
    loginPage = TC_Login.TestLoginOrangeHRM()
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.loginPage.driver = self.driver
    def test_a_make_leave_fulltime(self):
        self.loginPage.test_a_login_OrangeHRM_success()
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]").click()
        time.sleep(2)
        Leave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
        self.assertEqual(Leave_tag.text, "Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]").click()
        time.sleep(2)
        My_leave_list_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[1]/h5")
        self.assertEqual(My_leave_list_tag.text, "My Leave List")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/i").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click()
        time.sleep(2)
        self.driver.execute_script("scroll(0, 0);")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[1]/div").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/i").click()   #step 2
        time.sleep(2)
        driver.find_element(By.XPATH, "//*//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #pilih bulan cal2
        time.sleep(2)
        self.driver.execute_script("scroll(0, 0);")
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[53]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[31]/div").click() #click tanggal 31
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[3]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()
        time.sleep(2)
        leave_type = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div[3]/div/div[2]")
        self.assertEqual(leave_type.text, "CAN - Bereavement") 
        time.sleep(2)
        
        
        
    def tearDown(self): 
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
        