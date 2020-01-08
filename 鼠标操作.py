from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

browser = webdriver.Ie()
browser.get('http://www.baidu.com')
element = browser.find_element('css selector',"[name='wd']")
element3 = browser.find_elements_by_css_selector("[name='tj_settingicon']")[1]
element.send_keys('aaabbbccc')
action=ActionChains(browser)
#鼠标悬停
action.move_to_element(element3).perform()
#鼠标右键单击
action.context_click(element).perform()
#鼠标左键双击
action.double_click(element).perform()
#鼠标拖动元素1到元素2上
element1 = browser.find_element('css selector',"[name='wd']")
element2 = browser.find_element('css selector',"[name='wd']")
action.drag_and_drop(element1,element2).perform()
#拖动元素的偏移想X多少，Y多少
action.drag_and_drop_by_offset(element1,500,100)
sleep(5)
browser.quit()