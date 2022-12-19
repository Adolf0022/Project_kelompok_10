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
    def test_a_make_mytimesheet(self):
        self.loginPage.test_a_login_OrangeHRM_success()
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]").click() #click Time Menu 
        time.sleep(2)
        time_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]") #Validate time page 
        self.assertEqual(time_tag.text, "Time")
        time.sleep(2)
        timesheet_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]") #Validate time sheet page 
        self.assertEqual(timesheet_tag.text, "Timesheets")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span/i").click() #click Timesheet
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]").click() #click My Timesheet
        time.sleep(2)
        Mytimesheet_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[1]") #Validate My timsheet page
        self.assertEqual(Mytimesheet_tag.text, "My Timesheet")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/i").click() #click calender icon on time period text box 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #click list of months  
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #choose december
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #click list of years 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[53]").click() #choose 2022 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[3]/div[9]").click() #choose the date 
        time.sleep(2)
        Mytimesheet_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/div/div[1]/p") #Validate there isn't any time sheet
        self.assertEqual(Mytimesheet_tag.text, "No Timesheets Found")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button]").click() #click Creat Timesheet button
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate Toast message 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button]").click() #click Edit button
        time.sleep(2)
        Edittimesheet_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[1]/h6") #Validate edit time sheet page
        self.assertEqual(Edittimesheet_tag.text, "Edit Timesheet")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div/input").send_keys("Acme") #type project name
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/div/div[2]/div/div[2]/div").click() #choose Acme ltd - ACME Ltd
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div[1]/div[2]").click() #click activity Drop Down list 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/div/div[2]/div/div[2]/div[3]").click() #click activity bug fix
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[3]/div/div[2]/input").send_keys("10") #type 10 fist date
        time.sleep(2)
        driver.find_element(By.XPATH, "///*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[4]/div/div[2]/input").send_keys("10") #type 10 second date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[5]/div/div[2]/inputt").send_keys("9") #type 10 third date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[6]/div/div[2]/input").send_keys("9") #type 9 fourth date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[7]/div/div[2]/input").send_keys("10") #type 9 fifth date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[8]/div/div[2]/input").send_keys("9") #type 9 sixth date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[9]/div/div[2]/input").send_keys("9") #type 9 seventh date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[3]").click() #Click Save Button
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate Toast message 
        time.sleep(2)
        Mytimesheet_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[1]/div[1]") #Validate Back to My timsheet page
        self.assertEqual(Mytimesheet_tag.text, "My Timesheet")
        time.sleep(2)
        nameproject_tag = driver.find_element(By.XPATH, "//*[@id='app'/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[1]/span") #Validate Project
        self.assertEqual(nameproject_tag.text, "ACME Ltd - ACME Ltd")
        time.sleep(2)
        activity_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[2]/table/tbody/tr[1]/td[2]/span") #Validate Bug Fixes
        self.assertEqual(activity_tag.text, "Bug Fixes")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/form/div[3]/div[2]/button[2]]").click() #click submit button 
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate Toast message 
        time.sleep(2)
        
    def tearDown(self): 
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()