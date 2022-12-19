import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class Test_SEACRH_employee_failed(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_SEARCH_EMPLOYEE_failed(self):
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
        
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("234") #INPUT ID
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div/input').send_keys("mac") #INPUT supervisor name
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div[2]/div[1]/span' ).click() #choose supervisor
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[1]/input').send_keys("joko") #INPUT employee name
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[1]' ).click() #choose employee
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i' ).click() #drop down job title
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[3]' ).click() #choose job title
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[1]/div[2]/i' ).click() #drop down employee status
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]/span' ).click() #choose employee status
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[2]/i' ).click() #drop down include
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span' ).click() #choose include
        time.sleep(2)

        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]/i' ).click() #drop down sub unit
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[6]/span' ).click() #choose sub unit
        time.sleep(2)

        



        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]' ).click()
        time.sleep(5)


    
    




        def tearDown(self): 
            self.driver.close()
        
if __name__ == "__main__":
    unittest.main()