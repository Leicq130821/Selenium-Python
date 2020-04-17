from selenium import webdriver
from time import sleep
import unittest
# Fxieture由setUp(self)/tearDown(self)组成。
class Fixture(unittest.TestCase):
    # setUp会最先执行。
    def setUp(self):
        self.browser=webdriver.Ie()
        browser=self.browser
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get('http://localhost:9087')
    # tearDown会最后执行。
    def tearDown(self):
        browser=self.browser
        browser.switch_to.frame('topFrame')
        browser.find_element_by_link_text('退出系统').click()
        alert=browser.switch_to.alert
        alert.accept()
        sleep(3)
        browser.quit()
    # 每个test开头的方法执行都会先执行setUp()然后执行tearDown()。
    def testLoin1(self):
        browser=self.browser
        browser.find_element_by_id('username').send_keys('admin')
        browser.find_element_by_id('password').send_keys('000000')
        browser.find_element_by_tag_name('button').click()
        sleep(3)
    def testLoin2(self):
        browser=self.browser
        browser.find_element_by_id('username').send_keys('admin')
        browser.find_element_by_id('password').send_keys('000000')
        browser.find_element_by_tag_name('button').click()
        sleep(3)
if __name__ == '__main__':
    unittest.main()