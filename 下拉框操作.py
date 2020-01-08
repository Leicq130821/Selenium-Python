from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

browser = webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost/biz/user-login.html')
browser.find_element('css selector','#account').send_keys('admin')
browser.find_element('css selector',"input[name='password']").send_keys('000000')
browser.find_element('css selector','#submit').click()
browser.find_element_by_link_text('测试').click()
browser.find_element_by_link_text('Bug').click()
browser.find_element_by_link_text('提Bug').click()
selectelement=browser.find_element('id','type')
action = Select(selectelement)
#通过索引来查找下拉选项
action.select_by_index(2)
# 通过下拉选项的value值
action.select_by_value('性能问题')
# 通过下拉选项的显示文本
action.select_by_visible_text('代码问题')

browser.find_element_by_class_name('dropdown-toggle').click()
browser.find_element_by_link_text('签退').click()

sleep(3)
browser.quit()