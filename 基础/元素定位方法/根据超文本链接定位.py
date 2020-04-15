from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
# 通过文本类型的超链接进行定位(全匹配文本信息)。
browser.find_element_by_link_text('杭州盈丰软件股份有限公司').click()
# 通过文本类型的超链接进行定位(模糊匹配文本信息)。
browser.get('http://localhost:9087')
browser.find_element_by_partial_link_text('盈丰软件').click()

sleep(5)
browser.quit()