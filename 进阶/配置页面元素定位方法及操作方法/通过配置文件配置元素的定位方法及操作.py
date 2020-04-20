from selenium import webdriver
from time import sleep
import configparser

def login(*args):
    browser=webdriver.Ie()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('http://localhost:9087')
    for i in args:
        list=i.strip('[]').split(',')
        if list[2]=='1':
            browser.find_element(list[0],list[1]).send_keys(list[3])
        elif list[2]=='2':
            browser.find_element(list[0], list[1]).click()
    sleep(3)
    browser.quit()
if __name__ == '__main__':
    config=configparser.ConfigParser()
    config.read(r'E:\Selenium-Python\进阶\配置页面元素定位方法及操作方法\login.ini')
    list=[]
    for i in config.items(config.sections()[0]):
        list.append(i[1])
    print(list)
    login(*list)