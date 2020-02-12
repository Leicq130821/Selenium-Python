from selenium import webdriver
from time import sleep
browser = webdriver.Ie()
browser.get('http://localhost:7003')
#元素的class属性
browser.find_elements_by_class_name('cssTextInput')[0].send_keys('admin')
#元素的class属性
browser.find_elements_by_class_name('cssTextInput')[1].send_keys('000000')
#属性的标签名称
browser.find_element_by_tag_name('button').click()
sleep(5)
browser.quit()