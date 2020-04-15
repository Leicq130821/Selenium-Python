from selenium import webdriver
from time import sleep

browser = webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
browser.find_element_by_name('username').send_keys('admin')
browser.find_element_by_id('password').send_keys('000000')
# 通过元素的标签名称进行定位。
browser.find_element_by_tag_name('button').click()

sleep(5)
browser.quit()