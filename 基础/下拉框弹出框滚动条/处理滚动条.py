from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
browser.find_element_by_id('username').send_keys('admin')
browser.find_element_by_id('password').send_keys('000000')
browser.find_element_by_tag_name('button').click()
sleep(3)
# webdriver没有提供直接控制滚动条的方法，需要借助js脚本实现对滚动条的控制。
# 控制滚动条的js脚本：window.scrollTo(x,y)，x为左右移动，y为上下移动，x/y皆为像素。
browser.switch_to.frame('content') # 需要注意滚动条所在的表单。
js='window.scrollTo(0,1000)'  # 上下滚动条拉到底部。
# 使用浏览器对象的execute_script()方法执行js脚本。
browser.execute_script(js)
sleep(3)
js='window.scrollTo(0,0)' # 滚动条回到初始位置。
browser.execute_script(js)

sleep(3)
browser.quit()