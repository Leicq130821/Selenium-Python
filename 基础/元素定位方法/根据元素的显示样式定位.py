from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
# 通过calss。
browser.find_element_by_css_selector('.inputq2').send_keys('admin')
# 通过id。
browser.find_element_by_css_selector('#password').send_keys('000000')
# 通过标签名称。
browser.find_element_by_css_selector('button').click()
sleep(3)

browser.get('http://localhost:9087')
# 通过属性。
browser.find_element_by_css_selector('[name="username"]').send_keys('admin')
browser.find_element_by_css_selector('input[id="password"]').send_keys('000000')
# 通过路径。
browser.find_element_by_css_selector('div>button').click()
sleep(3)

browser.get('http://localhost:9087')
# 属性的值开头。
browser.find_element_by_css_selector('input[id^="user"]').send_keys('admin')
# 属性的值结尾。
browser.find_element_by_css_selector('input[name$="word"]').send_keys('000000')
# 属性的值包含。
browser.find_element_by_css_selector('[class*="ginb"]').click()

sleep(3)
browser.quit()