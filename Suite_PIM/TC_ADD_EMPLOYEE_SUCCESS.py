import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Test_Add_employee(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_employee_failed(self):
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
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]' ).click() #VIEW PIM
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-header-container']/button[@type='button']" ).click() #BUTTON ADD 
        time.sleep(5)


        
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input').send_keys("Peter Mac Anderson") #INPUT FIRST NAME 
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input').send_keys("mac") #INPUT MIDDLE NAME
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input').send_keys("anderson") #INPUT MIDDLE NAME
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input').send_keys("0023") #INPUT ID EMPLOYEE
        time.sleep(2)
       


        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]' ).click()
        time.sleep(5)



        def tearDown(self): 
            self.driver.close()
        
if __name__ == "__main__":
    unittest.main()