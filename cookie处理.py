from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.get('http://localhost/biz/user-login.html')

cookie = {"windowWidth":"1366","windowHeight":"642","bugModule":"0","qaBugOrder":"id_desc","lang":"zh-cn","device":"desktop","theme":"default","feedbackView":"0","lastProduct":"1","preBranch":"0","preProductID":"1","zentaosid":"8aelgaolt212tisek3ri8qh2s7"}
browser.add_cookie(cookie)
sleep(3)
browser.refresh()

sleep(3)
browser.quit()