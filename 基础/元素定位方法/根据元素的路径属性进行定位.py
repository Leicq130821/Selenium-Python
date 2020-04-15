from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
# 通过元素的路径信息进行定位。
browser.find_element_by_xpath('//input[@name="username"]').send_keys('admin')
browser.find_element_by_xpath('//*[@id="password"and@name="password"]').send_keys('000000')
browser.find_element_by_xpath('//div/button').click()
sleep(3)
browser.get('http://localhost:9087')
browser.find_element_by_xpath('//input[starts-with(@name,"username")]').send_keys('admin')
browser.find_element_by_xpath('//input[contains(@id,"password")]').send_keys('000000')
browser.find_element_by_xpath('//*[@onclick]').click()

sleep(3)
browser.quit()