from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
# 通过元素的ID属性进行定位。
browser.find_element_by_id('username').send_keys('admin')
# 通过元素的NAME属性进行定位。
browser.find_element_by_name('password').clear()
browser.find_element_by_name('password').send_keys('000000')
# 通过元素的class属性进行定位。
browser.find_element_by_class_name('loginbtn').click()

sleep(5)
browser.quit()