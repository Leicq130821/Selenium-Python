from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('https://www.baidu.com')
# ActionChains(browser)实例化鼠标对象。
action=ActionChains(browser)
element=browser.find_element_by_xpath("//*[text()='更多产品']")
# 移动鼠标到元素上悬停(鼠标的所有操作都是由方法perform()执行)
action.move_to_element(element).perform()

sleep(3)
browser.quit()