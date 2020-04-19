from 进阶.封装登录退出功能.Browser import Browser
from 进阶.封装登录退出功能.Login import Login
from 进阶.封装登录退出功能.Logout import Logout

if __name__ == '__main__':
    browser=Browser().browser('Ie','http://localhost:9087')
    Login().login(browser,'admin','000000')
    Logout().logout(browser)