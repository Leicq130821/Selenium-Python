import unittest
from time import sleep
from selenium import webdriver

class chandao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://127.0.0.1/biz/user-login-L2Jpei8=.html')
    def tearDown(self):
        self.driver.quit()
    def test1(self):
        self.driver.find_element_by_css_selector('#account').send_keys('admin11')
        self.driver.find_element_by_css_selector("[name='password']").send_keys('000000')
        self.driver.find_element_by_css_selector('#submit').click()
        self.driver.switch_to.alert.accept()
        sleep(3)
    def test2(self):
        self.driver.find_element_by_css_selector('#account').send_keys('admin')
        self.driver.find_element_by_css_selector("[name='password']").send_keys('111111')
        self.driver.find_element_by_css_selector('#submit').click()
        self.driver.switch_to.alert.accept()
        sleep(3)
    def test3(self):
        self.driver.find_element_by_css_selector('#account').send_keys('admin')
        self.driver.find_element_by_css_selector("[name='password']").send_keys('000000')
        self.driver.find_element_by_css_selector('#submit').click()
        self.driver.find_element_by_link_text('admin').click()
        self.driver.find_element_by_link_text('签退').click()
        sleep(3)
if __name__ == '__main__':
    unittest.main()