__author__ = 'Mahdy Vaio'
import unittest
from selenium import webdriver

class ClickAndSend(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)

    def test_ClickAndSend(self):
        driver = self.driver

        driver.get("http://www.amazon.com")

        #verification...........................................................
        logo = driver.find_element_by_css_selector(".nav-logo-base.nav-sprite")
        #1
        if logo is None:
            print 'Logo is not visible through None Method'
        else:
            print 'Logo is visible through None Method'

        #2
        if logo.text == "Amazon":
            print 'Logo is Visible through text method'
        else:
            print 'Logo is not visible through text method'

        #3
        if logo.is_displayed():
            print "Logo is visible through is_displayed method"
        else:
            print "Logo is not visible through is_displayed method"

        #send keywords.........................................................
        driver.find_element_by_css_selector("#twotabsearchtextbox").send_keys("ipad")

        #click and element.....................................................
        driver.find_element_by_css_selector(".nav-submit-input").click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()