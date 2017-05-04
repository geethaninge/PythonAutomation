from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import unittest 
import HTMLTestRunner  #for HTML report


class GoogleTest(unittest.TestCase):
  def setUp(self):
    #create new firefox session
    gecko_path =  'C:\My Dude\MyCodingWorkspace\geckodriver\geckodriver.exe'
    firefox_capabilities = DesiredCapabilities.FIREFOX
    firefox_capabilities['marionette'] = True
    self.driver = webdriver.Firefox(capabilities=firefox_capabilities,
                            executable_path=gecko_path) 
    #driver.implicitly_wait(30)
    self.driver.get("http://www.google.com/")
    #driver.maximize_window()

  def test_search_text(self):
    #driver=self.driver
    self.search_field = self.driver.find_element_by_name("q")
    self.search_field.send_keys("flower")
    self.search_field.submit()
    wait = WebDriverWait(self.driver,20)
    wait.until(EC.visibility_of_element_located((By.ID,"_Yvd")))
    #stitle = "flower"
    getTitle =self.driver.title
    self.assertIn("flower",getTitle)

  def tearDown(self):
    #close the browser window
    #driver =self.driver
    self.driver.quit()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)