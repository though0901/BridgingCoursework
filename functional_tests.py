from selenium import webdriver
import unittest


class FunctionalTestClass(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
