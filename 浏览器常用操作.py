from time import sleep
from selenium import webdriver
browser = webdriver.Ie()
browser.get('http://localhost:7003/')
sleep(3)
#设置浏览器大小
browser.set_window_size(200,200)
sleep(3)
#设置浏览器位置
browser.set_window_position(400,300)
sleep(3)
#最大化浏览器
browser.maximize_window()
sleep(3)
#浏览地址
browser.get('https://www.baidu.com/')
sleep(3)
#后退
browser.back()
sleep(3)
#前进
browser.forward()
sleep(3)
#刷新
browser.refresh()
sleep(3)
#截取浏览器当前页面并保存为
browser.get_screenshot_as_file(r"D:\测试工作\baidu.png")
sleep(3)
#关闭主页面
browser.close()