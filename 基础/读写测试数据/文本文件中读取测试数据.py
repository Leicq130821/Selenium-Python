from 基础.封装登录退出功能.Browser import Browser
from 基础.封装登录退出功能.Login import Login
from 基础.封装登录退出功能.Logout import Logout

if __name__ == '__main__':
    # 测试数据可以通过文本进行读取。
    with open(r'D:\自动化测试\browser.txt','r',encoding='utf-8') as file:
        data=file.read().split(',')
        print(data)
    with open(r'D:\自动化测试\user.txt','r',encoding='utf-8') as file:
        users=file.readlines()
        dict={}
        for user in users:
            dict.setdefault(user.strip().split(',')[0],user.strip().split(',')[1])
        print(dict)
    for key in dict.keys():
        browser = Browser().browser(data[0], data[1])
        Login().login(browser,key,dict[key])
        Logout().logout(browser)