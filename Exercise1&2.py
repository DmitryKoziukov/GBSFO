# -*- coding: utf-8 -*-
import unittest
import selenium
from selenium import webdriver



class Exercise(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("c:/exercise/driver/chromedriver.exe")

    def test_google1(self):
        self.driver.get('https://google.com')
        el = self.driver.find_element_by_name('q')
        el.send_keys('GBSFO')
        el.submit()
        href_arr = self.driver.find_elements_by_xpath("//div[@class='r']/a")

        for e in href_arr:
            if ((e.text.find("GBSFO")>-1) and (e.text.find("https://gbsfo.com/")>0)):
                lnk = e.get_attribute("href")
        print ("Opening "+lnk)
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(lnk)        

    def test_google2(self):
        self.driver.get('https://google.com')
        el = self.driver.find_element_by_name('q')
        el.send_keys('GBSFO')
        el.submit()
        el=self.driver.find_element_by_id("hdtb-tls")
        el.click()
        el = self.driver.find_element_by_xpath("//div[@class='hdtb-mn-hd'][2]/span[@class='mn-dwn-arw']")
        #el = self.driver.find_element_by_css_selector('.hdtb-mn-hd:nth-child(5) > .mn-dwn-arw')
        self.driver.execute_script("arguments[0].click();", el)
        #el.click()
        el = self.driver.find_element_by_xpath("//a[contains(text(),'За час')]").click()    


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
