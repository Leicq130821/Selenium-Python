from selenium import webdriver
from time import sleep
import configparser

def login(*args):
    browser=webdriver.Ie()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('http://localhost:9087')
    # 循环取出数据。
    for i in args:
        # 拆分列表元素。
        list=i.split(',')
        if list[2]=='1':
            browser.find_element(list[0],list[1]).send_keys(list[3])
        elif list[2]=='2':
            browser.find_element(list[0], list[1]).click()
    sleep(3)
    browser.quit()
if __name__ == '__main__':
    # 实例化配置文件对象。
    config=configparser.ConfigParser()
    # 读取配置文件信息。
    config.read(r'E:\Selenium-Python\进阶\配置页面元素定位以及元素操作\login.ini')
    list=[]
    # 取出节点的value值组装成一个列表。
    for i in config.items(config.sections()[0]):
        list.append(i[1])
    login(*list)