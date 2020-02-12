import unittest
from selenium import webdriver
import time
import sys

class Test(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Ie()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://localhost/biz/user-login.html')
    def test1(self):
        driver=self.driver
        driver.find_element_by_css_selector('#account').send_keys('admin')
        driver.find_element_by_css_selector('[name="password"]').send_keys('111111')
        driver.find_element_by_css_selector('#submit').click()
        alert=driver.switch_to.alert
        text=alert.text
        print(text)
        alert.accept()
        try:
            #断言
            self.assertIn('登陆失败1',text)
        except AssertionError:
            #获取时间戳
            nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")
            #获取错误信息
            Error=sys.exc_info()[1]
            print(Error)
            #截图报存（有弹出框存在时貌似不能截图成功，需要处理弹出框后才能截图）
            driver.get_screenshot_as_file("./image/%s--%s.png"%(nowtime,Error))
            #抛出错误
            raise AssertionError
    def tearDown(self):
        driver=self.driver
        driver.quit()
if __name__ == '__main__':
    unittest.main()