from selenium import webdriver
from time import sleep

class Browser():
    def browser(self,browser,url):
        if browser=='Ie':
            self.browser=webdriver.Ie()
        elif browser=='FireFox':
            self.browser=webdriver.Firefox()
        elif browser=='Chrome':
            self.browser=webdriver.Chrome()
        else:
            raise ValueError('输入的浏览器不存在！')
        browser=self.browser
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get(url)
        sleep(3)
        return browser