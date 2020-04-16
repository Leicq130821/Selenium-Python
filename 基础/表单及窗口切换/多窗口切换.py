from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
browser.find_element_by_xpath('//input[@id="username"and@name="username"]').send_keys('admin')
browser.find_element_by_css_selector('input[id="password"]').send_keys('000000')
browser.find_element_by_css_selector('button').click()
sleep(3)
browser.switch_to.frame('topFrame')
# browser.current_window_handle：获取当前页面句柄。
current=browser.current_window_handle
print(current)
browser.find_element_by_link_text('19029-金谷·锐泰6号资金信托计划').click()
# browser.window_handles：获取所以句柄。
handles=browser.window_handles
print(handles)
# browser.switch_to.window(handle)：通过句柄来切换窗口（最后一个句柄是当前最新窗口的句柄）。
browser.switch_to.window(handles[-1])
current=browser.current_window_handle
print(current)
sleep(3)
browser.find_element_by_name('query_product_name').send_keys('6')
browser.find_element_by_name('btnSosuo').click()
# JS控制div垂直滚动条位置。
js="document.getElementsByTagName('div')[3].scrollTop=1200"
browser.execute_script(js)
sleep(3)
browser.find_element_by_id('btnCancel').click()
browser.switch_to.window(handles[0])
browser.switch_to.frame('topFrame')
browser.find_element_by_link_text('退出系统').click()
alert=browser.switch_to.alert
alert.accept()

sleep(3)
browser.quit()