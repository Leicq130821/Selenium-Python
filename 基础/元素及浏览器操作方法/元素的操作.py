from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
username=browser.find_element_by_id('username')
password=browser.find_element_by_id('password')
login=browser.find_element_by_tag_name('button')
# 元素某个元素的值。
print('class属性的值:',login.get_attribute('class'))
# 元素的标签名称。
print('元素的标签名称:',login.tag_name)
# 元素的尺寸。
print('元素的尺寸(像素):',login.size)
# 元素的文本信息。
print('元素的文本信息:',login.text)
# 元素的坐标。
print('元素的坐标(像素):',login.location)
# 元素是否可见。
print('元素是否可见:',login.is_displayed())
# 元素是否可用。
print('元素是否可用:',login.is_enabled())
# 元素是否被选中。
print('元素是否被选中:',login.is_selected())
# 输入文本信息。
username.send_keys('admin')
password.send_keys('000000')
# 清除文本信息。
password.clear()
password.send_keys('000000')
# 点击。
login.click()

sleep(5)
browser.quit()