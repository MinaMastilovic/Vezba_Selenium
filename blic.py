import unittest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

class TestBlicRs(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome(r"C:\Users\masti\OneDrive\Documents\Desktop\webdriver\chromedriver.exe")
        self.driver.maximize_window()
        

    def testVesti (self):
        self.driver.get("https://www.blic.rs")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_link_text("Vesti").click()
        assert "Itt will open Vesti" not in self.driver.page_source

    def testSport(self):
        self.driver.get("https://www.blic.rs/")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_link_text("Sport").click()
        assert "Itt will open Sport" not in self.driver.page_source

    def testZabava(self):
        self.driver.get("https://www.blic.rs/")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_link_text("Sport").click()
        assert "Itt will open Zabava" not in self.driver.page_source

    def testBiznis(self):
        self.driver.get("https://www.blic.rs/")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_link_text("Biznis").click()
        assert "Itt will open Biznis" not in self.driver.page_source

    def testKultura(self):
        self.driver.get("https://www.blic.rs/")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_link_text("Kultura").click()
        assert "Itt will open Kultura" not in self.driver.page_source

    def testSlobodnovreme(self):
        self.driver.get("https://www.blic.rs/")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_link_text("Slobodno vreme").click()
        assert "Itt will open Slobodno vreme" not in self.driver.page_source
        time.sleep(3)

    def testŽena(self):
        self.driver.get("https://www.blic.rs/")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_xpath("//nav[@class='menu__main']//a[contains(text(),'ena')]").click()
        assert "Itt will open Žena" not in self.driver.page_source

    def testTritacke(self):
        self.driver.get("https://www.blic.rs/")
        assert "Blic" in self.driver.title
        self.driver.find_element_by_xpath("//li[@class='dots']//i[1]").click()
        self.driver.find_element_by_xpath("//ul[@class='menu__more']//a[contains(text(),'Auto')]").click()
        assert "Itt will open Auto" not in self.driver.page_source



    def tearDown(self):
        self.driver.close()

if __name__ == "main":
    unittest.main()


