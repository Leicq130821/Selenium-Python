from time import sleep
from selenium import webdriver

browser = webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost/biz/user-login.html')
browser.find_element('css selector','#account').send_keys('admin')
browser.find_element('css selector',"input[name='password']").send_keys('000000')
browser.find_element('css selector','#submit').click()
tanchukuang = browser.switch_to.alert
#弹出框文本
print(tanchukuang.text)
#接受弹出框
tanchukuang.accept()
#拒绝/取消弹出框
tanchukuang.dismiss()

sleep(3)
browser.quit()