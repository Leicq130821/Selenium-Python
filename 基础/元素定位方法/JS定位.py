from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('http://localhost:9087')
# 通过id属性。
username="document.getElementById('username').value='admin'"
browser.execute_script(username)
# 通过name属性。
password="document.getElementsByName('password')[0].value='000000'"
browser.execute_script(password)
# 通过标签名称。
login="document.getElementsByTagName('button')[0].click()"
browser.execute_script(login)
sleep(3)
browser.get('https://www.baidu.com')
# 通过calss属性。
text="document.getElementsByClassName('s_ipt')[0].value='测试啦'"
browser.execute_script(text)
button="document.getElementsByClassName('bg s_btn')[0].click()"
browser.execute_script(button)
sleep(3)
browser.get('http://www.baidu.com')
# 通过css定位。
text="document.querySelector('#kw').value='我又测试啦'"
browser.execute_script(text)
# css复数形式。
button="document.querySelectorAll('#su')[0].click()"
browser.execute_script(button)

sleep(3)
browser.quit()