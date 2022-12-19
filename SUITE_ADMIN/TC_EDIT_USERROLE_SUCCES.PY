import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class test_EDIT_userrole_success(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_EDIT_a_userorle(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") #OPEN BROWSER
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin") #INPUT USERNAME
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin123") #INPUT PASSWORD
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div[@class='orangehrm-login-layout-blob']//form[@action='/web/index.php/auth/validate']/div[3]/button[@type='submit']").click()    #CLICK BUTTON LOGIN
        time.sleep(2)  
        driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/dashboard/index']/span[.='Dashboard']" ) #VIEW DASHBOARD
        time.sleep(2)                               
        driver.find_element(By.XPATH, "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/admin/viewAdminModule']" ).click() #VIEW ADMIN
        time.sleep(4)
        driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[6]/div/button[2]/i" ).click() #buuton edit
        time.sleep(5)

        # driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]/div[2]/i").click() #dropdown userrole
        # time.sleep(2)
        # driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click() #choose Admin
        # time.sleep(2)
        
        # driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[1]/div[2]").click() #dropdown STATUS
        # time.sleep(2)
        # driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[2]").click() #choose enabled
        # time.sleep(2)
        
        
        # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys("Odis Adalwin") #INPUT employee
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').send_keys(Keys.ENTER) #TAKE A VALUES USERNAME
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input').click() #CLICK VALUES
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input').send_keys("peterpan") #INPUT USERNAME
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input').send_keys("Peterpan1245_") #INPUT password
        # time.sleep(2)
        # driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input').send_keys("Peterpan1245_")#INPUT CONFIRMATION PASSWORD
        # time.sleep(2)


        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]' ).click() #BUTTON SAVE
        time.sleep(5)

        def tearDown(self): 
            self.driver.close()
        
if __name__ == "__main__":
    unittest.main()