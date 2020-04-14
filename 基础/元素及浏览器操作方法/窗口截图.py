from selenium import webdriver
from time import sleep

browser = webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:7003/')
browser.find_element_by_css_selector('#username').send_keys('admin')
browser.find_element_by_css_selector("[name='password']").send_keys('000000')
browser.find_element_by_css_selector('button').click()

browser.get_screenshot_as_file('E:\业务系统.png')

sleep(5)
browser.quit()