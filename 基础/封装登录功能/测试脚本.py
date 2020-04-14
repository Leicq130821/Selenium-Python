from 基础.封装登录功能.browser import Browser
from 基础.封装登录功能.login import Login
from 基础.封装登录功能.usefile import Openfile
import unittest
from time import sleep

class Test(unittest.TestCase):
    def testreaddata(bpath,upath):
        browser=Openfile.getbrowser(bpath)
        user=Openfile.getuser(upath)
        return browser,user
    def testopenbrowser(browser):
        driver=Browser.WEB(browser)
        Browser.URL(driver,browser)
        return driver
    def testlogin_sql(driver,user):
        Login.login_sql(driver,user)
        sleep(5)
        driver.quit()
    def testlogin_excel(driver,excel):
        Login.login_excel(driver,excel)
        sleep(5)
        driver.quit()
if __name__ == '__main__':
    bpath=r'E:\testdata\browser.txt'
    upath=r'E:\testdata\user.txt'
    excel=r'E:\testdata\user.xls'
    browser,user=Test.testreaddata(bpath,upath)
    driver=Test.testopenbrowser(browser)
    # Test.testlogin_sql(driver,user)
    Test.testlogin_excel(driver,excel)