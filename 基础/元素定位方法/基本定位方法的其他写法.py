from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
# find_element('方法名','参数值')。
browser.find_element('id','username').send_keys('admin')
browser.find_element('xpath','//input[@name="password"]').send_keys('000000')
browser.find_element('css selector','button').click()
sleep(3)

browser.get('http://localhost:9087')
# find_element(By.方法大写,'参数值')。
browser.find_element(By.NAME,'username').send_keys('admin')
browser.find_element(By.CSS_SELECTOR,'[id="password"]').send_keys('000000')
browser.find_element(By.TAG_NAME,'button').click()

sleep(3)
browser.quit()