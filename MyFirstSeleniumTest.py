__author__ = 'Mahdy Vaio'
import unittest
from selenium import webdriver

class MyFirstSeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(15)

    def test_ProductVisibility(self):
        driver = self.driver
        success = True

        driver.get("http://www.amazon.com/")
        cart = driver.find_element_by_css_selector("#nav-cart").is_displayed()

        if cart:
            print "Cart is visible"
        else:
            success = False
            print "Cart is not visible"

        self.assertTrue(success)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()