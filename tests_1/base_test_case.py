import unittest
import time
from selenium import webdriver


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\gecko\geckodriver.exe')
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get("https://pl.tripadvisor.com/")

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
