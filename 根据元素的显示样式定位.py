from time import sleep
from selenium import webdriver
browser = webdriver.Ie()
browser.get('http://localhost:7003')
#通过元素的ID属性
browser.find_element_by_css_selector('#username').send_keys('admin')
#通过元素的CLASS属性
browser.find_elements_by_css_selector('.cssTextInput')[1].send_keys('000000')
#通过元素的标签名称
browser.find_element_by_css_selector('button').click()
browser.get('http://localhost:7003')
#通过元素的属性
browser.find_element_by_css_selector("[tabIndex='1']").send_keys('admin')
browser.find_element_by_css_selector("[tabIndex='2']").send_keys('000000')
#通过元素的路径
browser.find_element_by_css_selector("p>button").click()
browser.get('http://localhost:7003')
#元素的name属性的值开头为u
browser.find_element_by_css_selector("input[name^='u']").send_keys('admin')
#元素的name属性的值结尾为d
browser.find_element_by_css_selector("[name$='d']").send_keys('000000')
#元素的type属性的值包含b
browser.find_element_by_css_selector("[type*='b']").click()
sleep(5)
browser.quit()