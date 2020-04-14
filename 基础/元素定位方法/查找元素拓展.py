from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Ie()
browser.get('http://localhost:7003/')
#find_element_by('方法','参数')
browser.find_element('id','username').send_keys('admin')
browser.find_element('name','password').send_keys('000000')
browser.find_element('css selector','button').click()
browser.back()
browser.get('http://localhost:7003/')
#通By类：find_element(By.方法,'参数')
browser.find_element(By.ID,'username').send_keys('admin')
browser.find_element(By.NAME,'password').send_keys('000000')
browser.find_element(By.CSS_SELECTOR,'button').click()
browser.quit()