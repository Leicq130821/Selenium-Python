from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Ie()
browser.get('http://www.baidu.com/')
element=browser.find_element_by_css_selector('#kw')
element.send_keys('123456')
element.send_keys(Keys.CONTROL,'a')
element.send_keys(Keys.CONTROL,'x')
element.send_keys(Keys.CONTROL,'v')
element.send_keys(Keys.BACK_SPACE)
sleep(5)
browser.quit()