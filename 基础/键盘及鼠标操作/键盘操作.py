from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
element=browser.find_element_by_id('username')
element.send_keys('a')
sleep(3)
# 键盘操作需要调用元素的send_keys()方法。
element.send_keys(Keys.BACK_SPACE)
element.send_keys('admin')
# 组合键盘用逗号隔开(键盘字母需要用小写)。
element.send_keys(Keys.CONTROL,'a')
element.send_keys(Keys.CONTROL,'x')
sleep(3)
element.send_keys(Keys.CONTROL,'v')

sleep(3)
browser.quit()