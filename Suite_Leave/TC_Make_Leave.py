import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import TC_Login

class TestMakeLeave(unittest.TestCase):
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
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
        time.sleep(2)
        ApplyLeave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6")
        self.assertEqual(ApplyLeave_tag.text, "Apply Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(2)
        select_can = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
        self.assertEqual(select_can.text, "CAN - Bereavement")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[27]").click() #pilih tanggal 27
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/i").click() #pilih tanggal cal 2
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #pilih bulan pada calende ke-2 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[27]").click() #pilih tanggal 27
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']")
        time.sleep(2)
        
    def test_b_make_leave_halfday_morning(self):
        self.loginPage.test_a_login_OrangeHRM_success()
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]").click()
        time.sleep(2)
        Leave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
        self.assertEqual(Leave_tag.text, "Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
        time.sleep(2)
        ApplyLeave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6")
        self.assertEqual(ApplyLeave_tag.text, "Apply Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(2)
        select_can = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
        self.assertEqual(select_can.text, "CAN - Bereavement")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[29]").click() #pilih tanggal 29
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/i").click() #click calender to Date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #pilih bulan pada calende ke-2 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[29]").click() #pilih tanggal 29
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div/div[2]").click() #pilih durasi
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[2]/div[2]").click() #click half-day morning
        time.sleep(2)
        half_day_moring = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div")
        self.assertEqual(half_day_moring.text, "Half Day - Morning")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']")
        time.sleep(2)
        
    def test_c_make_leave_halfday_afternoon(self):
        self.loginPage.test_a_login_OrangeHRM_success()
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]").click()
        time.sleep(2)
        Leave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
        self.assertEqual(Leave_tag.text, "Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
        time.sleep(2)
        ApplyLeave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6")
        self.assertEqual(ApplyLeave_tag.text, "Apply Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(2)
        select_can = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
        self.assertEqual(select_can.text, "CAN - Bereavement")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #dropdown bulan
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() # drop down tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[30]").click() #pilih tanggal 30
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/i").click() #click calender to Date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #pilih bulan pada calende ke-2 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[30]").click() #pilih tanggal 30
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div/div[2]").click() #pilih durasi
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[2]/div[3]").click() #click half-day afternoon
        time.sleep(2)
        half_day_moring = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div")
        self.assertEqual(half_day_moring.text, "Half Day - Afternoon")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button").click()
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']")
        time.sleep(2)
        
    def test_d_make_leave_by_specifictime(self):
        self.loginPage.test_a_login_OrangeHRM_success()
        driver = self.driver
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]").click()
        time.sleep(2)
        Leave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6")
        self.assertEqual(Leave_tag.text, "Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]").click()
        time.sleep(2)
        ApplyLeave_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6")
        self.assertEqual(ApplyLeave_tag.text, "Apply Leave")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[2]/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div[2]/div[2]").click()
        time.sleep(2)
        select_can = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div")
        self.assertEqual(select_can.text, "CAN - Bereavement")
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[3]/div[22]").click() #pilih tanggal 22
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div/i").click() #click calender to Date
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/div/i").click() #pilih bulan pada calende ke-2 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[1]/ul/li[12]").click() #pilih bulan desember
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/div/i").click() #pilih tahun
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]/ul/li[51]").click() #click tahun 2022
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[3]/div[22]").click() #pilih tanggal 22
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div/div[2]").click() #pilih durasi
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div/div[2]/div[4]").click() #click specify time
        time.sleep(2)
        Specify_time = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/div") #validate specify time
        self.assertEqual(Specify_time.text, "Specify Time")
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/i").click() #click timer on from textbox 
        time.sleep(1)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[2]/div[1]/input").send_keys("01")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/input").send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[2]/div[3]/input").send_keys("30")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div[2]/div[4]/div[2]").click() #Choose am or pm
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/div/div[1]/i").click() #click timer on  textbox 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/div/div[2]/div[1]/input").send_keys(Keys.CONTROL + "a")#set the hour
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/div/div[2]/div[1]/input").send_keys("05")
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/div/div[2]/div[3]/input").send_keys(Keys.CONTROL + "a") #set the minutes
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/div/div[2]/div[3]/input").send_keys("30") 
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/div/div[2]/div/div[2]/div[4]/div[2]").click() #Choose am or pm
        time.sleep(2)
        
        
    def tearDown(self): 
        self.driver.close()
        
        
if __name__ == "__main__":
    unittest.main()
