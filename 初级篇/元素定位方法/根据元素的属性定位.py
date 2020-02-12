from time import sleep
from selenium import webdriver
browser = webdriver.Ie()
browser.get('http://localhost:7003/')
#元素的id属性
browser.find_element_by_id('username').send_keys('admin')
#元素的name属性
browser.find_element_by_name('password').send_keys('000000')
#元素的class属性
browser.find_element_by_class_name('cssLoginBtn_L1').click()
sleep(5)
browser.quit()