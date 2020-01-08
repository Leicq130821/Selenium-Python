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
browser.find_elements('css selector',"a[tabindex='-1']")[4].click()
browser.find_element('css selector',"li[title='安全相关']").click()

sleep(3)
browser.quit()