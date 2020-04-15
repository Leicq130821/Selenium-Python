from selenium import webdriver
from time import sleep

browser=webdriver.Ie()
# 设置浏览器窗口尺寸。
browser.set_window_size(500,500)
# 设置浏览器位置。
browser.set_window_position(400,400)
# 浏览器窗口最大化。
browser.maximize_window()
# 访问网页。
browser.get('https://www.baidu.com')
# 刷新页面。
browser.refresh()
browser.get('http://localhost:9087')
# 后退。
browser.back()
# 前进。
browser.forward()
# 页面的标题。
print('页面的标题:',browser.title)
# 页面的url。
print('页面的url:',browser.current_url)
# 截取当前页面图并保存为。
browser.get_screenshot_as_file(r'D:\自动化测试\首页截图.png')
# 关闭当前页面。
browser.close()
# 关闭由webdriver打开的页面。
# browser.quit()