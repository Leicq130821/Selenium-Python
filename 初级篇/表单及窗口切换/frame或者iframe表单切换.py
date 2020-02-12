from selenium import webdriver
from time import sleep


browser = webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:7003')
browser.find_element('css selector','#username').send_keys('admin')
browser.find_element('css selector','#password').send_keys('000000')
browser.find_element('css selector','button').click()
browser.switch_to.frame('topFrame')
browser.find_element_by_link_text('当前产品').click()
browser.switch_to.default_content()
browser.switch_to.frame('leftFrame')
browser.switch_to.frame('leftiframe')
browser.find_element_by_link_text('前台业务').click()
browser.switch_to.default_content()
browser.switch_to.frame('topFrame')
browser.find_element('css selector',"img[title='退出系统']").click()
action = browser.switch_to.alert
action.accept()

sleep(5)
browser.quit()