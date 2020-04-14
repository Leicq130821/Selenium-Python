from time import sleep
from selenium import  webdriver
browser = webdriver.Ie()
browser.get('https://www.baidu.com')
#全称超文本链接
browser.find_element_by_link_text('新闻').click()
browser.back()
#模糊超文本链接
browser.find_element_by_partial_link_text('12').click()
sleep(5)
browser.quit()