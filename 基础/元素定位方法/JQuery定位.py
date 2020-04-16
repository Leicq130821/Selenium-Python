from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
browser.maximize_window()
browser.implicitly_wait(5)
browser.get('https://www.baidu.com')
# jQuery定位的基本语法是：$(selector).action()，selector与JavaScript的选择器querySelector定位写法差不多，action()常用的是写入文本值val(value)以及单击click()。
username="$('.s_ipt').val('测试测试测试')"
browser.execute_script(username)
password="$('#su').click()"
browser.execute_script(password)

sleep(3)
browser.quit()