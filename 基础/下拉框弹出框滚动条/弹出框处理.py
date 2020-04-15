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
browser.switch_to.frame('topFrame')
browser.find_element_by_link_text('退出系统').click()
# 切换到弹出框。
alert=browser.switch_to.alert
# 获取弹出框的文本信息。
print(alert.text)
# 拒绝弹出框信息。
alert.dismiss()
browser.find_element_by_link_text('退出系统').click()
alert=browser.switch_to.alert
# 接受弹出框信息。
alert.accept()

sleep(3)
browser.quit()