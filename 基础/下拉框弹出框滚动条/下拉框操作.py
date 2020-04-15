from selenium import webdriver
from selenium.webdriver.support.select import Select
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
browser.find_element_by_id('mmenu8').click()
browser.switch_to.default_content()
browser.switch_to.frame('leftFrame')
browser.switch_to.frame('leftiframe')
browser.find_element_by_id('itemTextLink5').click()
browser.find_element_by_id('itemTextLink9').click()
browser.switch_to.default_content()
browser.switch_to.frame('content')
browser.find_element_by_id('btnNew').click()
handles=browser.window_handles
browser.switch_to.window(handles[-1])
element=browser.find_element_by_name('proj_mem_role')
# options=Select(element):实例化下拉框对象。
options=Select(element)
# 通过下拉选项的索引选择下拉选项。
options.select_by_index(1)
# 通过下拉选项的value值选择下拉选项。
options.select_by_value('02')
# 通过下拉选项显示的文本信息选择下拉选项。
options.select_by_visible_text('项目分管领导')

sleep(3)
browser.quit()