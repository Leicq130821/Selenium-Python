from selenium import webdriver
from time import sleep
import pymssql

def login(*args):
    browser=webdriver.Ie()
    browser.maximize_window()
    browser.implicitly_wait(5)
    browser.get('http://localhost:9087')
    # 循环取出数据。
    for tuple in args:
        if tuple[2]==1:
            browser.find_element(tuple[0],tuple[1]).send_keys(tuple[3])
        elif tuple[2]==2:
            browser.find_element(tuple[0], tuple[1]).click()
    sleep(3)
    browser.quit()
if __name__ == '__main__':
    # 建立数据库连接。
    with pymssql.connect('127.0.0.1:1433','sa','000000','TEST') as sql:
        # 实例化数据库索引。
        with sql.cursor() as cursor:
            # 查询数据。
            cursor.execute('SELECT FUNCITON_ELEMENT_SELECT,FUNCITON_ELEMENT_SELECT_KEY,FUNCITON_ELEMENT_ACTION,FUNCITON_ELEMENT_ACTION_KEY FROM DICTPARAM WHERE FUNCTION_ID=1')
            # 从索引中取出所查的数据（数据结果为一个列表）。
            list=cursor.fetchall()
    login(*list)