from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import unittest
from datetime import datetime

class Test(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Ie()
        browser=self.browser
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get('http://localhost:9087')
        browser.find_element_by_id('username').send_keys('admin')
        browser.find_element_by_id('password').send_keys('000000')
        browser.find_element_by_tag_name('button').click()
        sleep(3)
    def test(self):
        try:
            browser=self.browser
            browser.switch_to.frame('topFrame')
            browser.find_element_by_link_text('集团报送').click()
            browser.switch_to.default_content()
            browser.switch_to.frame('leftFrame')
            browser.switch_to.frame('leftiframe')
            browser.find_element_by_link_text('信托上报信息').click()
            browser.find_element_by_id('itemTextLink9').click()
            browser.switch_to.default_content()
            browser.switch_to.frame('content')
            browser.find_element_by_css_selector('input[value=496]').click()
            browser.find_element_by_css_selector('button[title="作废 "]').click()
            alert=browser.switch_to.alert
            alert.accept()
            sleep(3)
            alert=browser.switch_to.alert
            alert.accept()
            browser.find_element_by_id('queryButton').click()
            element=browser.find_element_by_css_selector('select[name="delete_flag"]')
            options=Select(element)
            options.select_by_value('1')
            browser.find_element_by_name('btnQuery').click()
            element=browser.find_element_by_name('serial_no')
            value=element.get_attribute('value')
            self.assertEqual(value,'496','项目成员信息作废失败')
        except Exception as E:
            print(E)
            browser.get_screenshot_as_file(r'D:\自动化测试\失败%s.png'%datetime.now().strftime('%Y年%m月%d日 %H点%M分%S秒'))
        else:
            browser.get_screenshot_as_file(r'D:\自动化测试\成功%s.png'%datetime.now().strftime('%Y年%m月%d日 %H点%M分%S秒'))
        finally:
            browser.switch_to.default_content()
    def tearDown(self):
        browser=self.browser
        browser.switch_to.frame('topFrame')
        browser.find_element_by_link_text('退出系统').click()
        alert=browser.switch_to.alert
        alert.accept()
        sleep(3)
        browser.quit()
if __name__ == '__main__':
    unittest.main()

