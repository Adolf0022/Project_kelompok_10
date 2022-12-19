import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import TC_Login

class TestTimeMenu(unittest.TestCase):
    loginPage = TC_Login.TestLoginOrangeHRM()
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.loginPage.driver = self.driver
    def test_a_make_mypunch_in_out(self):
        self.loginPage.test_a_login_OrangeHRM_success()
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]").click() #click Time Menu 
        time.sleep(2)
        time_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]") #Validate time page 
        self.assertEqual(time_tag.text, "Time")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click() #click sub attendance
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]/a").click() #click punch
        time.sleep(2)
        Punch_in_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6") #Validate punch in page
        self.assertEqual(Punch_in_tag.text, "Punch In")
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[1]/i").click() #click calender icon
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #click list of months  
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #choose december
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #click list of years 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[53]").click() #choose 2022 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[6]").click() #choose the date 6
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/i").click() #click clock icon
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys(Keys.CONTROL + "a") #input hour in
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys("08")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/input").send_keys(Keys.CONTROL + "a") #input minutes in
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/input").send_keys("00")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[4]/div[1]/input").click() #Choose am for in
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/i").click() #click clock icon to close set tim 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button").click() #Click "In" Button
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate Toast message 
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6") #Validate punch out page 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/i").click() #click calender icon
        time.sleep(2)
        driver.find_element(By.XPATH, "///*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #click list of months  
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app'/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #choose december
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #click list of years 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[53]").click() #choose 2022 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[6]").click() #choose the date 6
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/i").click() #click clock icon
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys(Keys.CONTROL + "a") #input hour in
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys("06")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/input").send_keys(Keys.CONTROL + "a") #input minutes in
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div[2]/div[3]/input").send_keys("00")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[4]/div[2]").click() #Choose pm for out
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/i").click() #click clock icon to close set tim 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/form/div[3]/button").click() #Click "Out" Button
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate Toast message 
        time.sleep(2)
        Punch_in_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6") #Validate back to punch in page
        self.assertEqual(Punch_in_tag.text, "Punch In")
        time.sleep(5)
        
        

        
    def tearDown(self): 
        self.driver.close()
        
        
if __name__ == "__main__":
    unittest.main()    