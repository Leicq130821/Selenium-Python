from time import sleep
from selenium import webdriver

browser = webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost/biz/user-login.html/')
browser.find_element('css selector','#account').send_keys('admin')
browser.find_element('css selector',"input[name='password']").send_keys('000000')
browser.find_element('css selector','#submit').click()
sleep(2)
JS1="window.scrollTo(0,1000)"
JS2="window.scrollTo(0,0)"
browser.execute_script(JS1)
sleep(2)
browser.execute_script(JS2)
sleep(2)
browser.find_element('css selector','.dropdown-toggle').click()
browser.find_element_by_link_text('签退')

sleep(5)
browser.quit()