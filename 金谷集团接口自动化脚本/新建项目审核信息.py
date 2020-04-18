from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select
import unittest

class Addnew(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Ie()
        browser=self.browser
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get('http://localhost:9087')
        browser.find_element_by_name('username').send_keys('admin')
        browser.find_element_by_id('password').clear()
        browser.find_element_by_id('password').send_keys('000000')
        browser.find_element_by_tag_name('button').click()
        sleep(3)
    def test_TPROJ_CHECK_INFO(self):
        browser=self.browser
        browser.switch_to.frame('topFrame')
        browser.find_element_by_id('mmenu8').click()
        browser.switch_to.default_content()
        browser.switch_to.frame('leftFrame')
        browser.switch_to.frame('leftiframe')
        browser.find_element_by_id('itemTextLink5').click()
        browser.find_element_by_css_selector('#itemTextLink12').click()
        browser.switch_to.default_content()
        browser.switch_to.frame('content')
        browser.find_element_by_name('btnNew').click()
        handles=browser.window_handles
        print(handles)
        browser.switch_to.window(handles[-1])
        sleep(2)
        selectelement1=browser.find_element_by_name('proj_id')
        option1=Select(selectelement1)
        option1.select_by_index(1)
        browser.find_element_by_name('proj_check_seq').send_keys('XMSHLS0001')
        browser.find_element_by_name('proj_check_comnt').send_keys('项目审核通过')
        selectelement2=browser.find_element_by_name('checker_empno_name')
        option2=Select(selectelement2)
        option2.select_by_index(1)
        browser.find_element_by_name('checker_mem_role').send_keys('项目经理')
        browser.find_element_by_name('checker_mem_check_comnt').send_keys('审核人员通过')
        browser.find_element_by_name('reg_person').send_keys('李明')
        browser.find_element_by_name('reg_org').send_keys('金谷信托')
        browser.find_element_by_name('reg_tm_picker').send_keys('20200416')
        browser.find_elements_by_name('btnSave')[0].click()
        browser.switch_to.window(handles[0])
        sleep(3)
        alert=browser.switch_to.alert
        alert.accept()
        sleep(3)
    def tearDown(self):
        browser=self.browser
        browser.switch_to.default_content()
        browser.switch_to.frame('topFrame')
        browser.find_element_by_link_text('退出系统').click()
        alert=browser.switch_to.alert
        alert.accept()
        sleep(3)
        browser.quit()
if __name__ == '__main__':
    unittest.main()