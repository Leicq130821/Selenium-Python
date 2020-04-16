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
# 通过调用浏览器对象的switch_to.frame(name/id)方法切换到frame或者iframe表单中，name/id为frame/iframe元素的name/id属性值。
browser.switch_to.frame('topFrame')
browser.find_element_by_id('mmenu8').click()
# 通过调用浏览器对象的switch_to.default_content()方法切换回默认主页面。
browser.switch_to.default_content()
# 层层嵌套的frame/iframe页面需要层层切换。
browser.switch_to.frame('leftFrame')
browser.switch_to.frame('leftiframe')
browser.find_element_by_id('itemTextLink5').click()
browser.find_element_by_id('itemTextLink6').click()
# 如果frame/iframe没有id、name属性则先定位到frame/iframe元素，然后通过switch_to(frame/iframe)的方法切换到frame/iframe表单。
browser.switch_to.default_content()
frame=browser.find_element_by_css_selector('frame[name="content"]')
browser.switch_to.frame(frame)
browser.find_element_by_css_selector('#btnNew').click()

sleep(3)
browser.quit()