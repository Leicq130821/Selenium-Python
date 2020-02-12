from selenium import webdriver
from time import sleep

browser = webdriver.Firefox()
browser.maximize_window()
browser.implicitly_wait(5)

browser.get('https://www.baidu.com/')
browser.find_element_by_css_selector("#kw").send_keys('网易云课堂')
sleep(2)
browser.find_element_by_css_selector("input[id='su']").click()
jubings=browser.window_handles
browser.find_element_by_partial_link_text('我的职业课堂').click()
jubing=browser.current_window_handle

browser.switch_to.window(jubing)

sleep(5)
browser.quit()