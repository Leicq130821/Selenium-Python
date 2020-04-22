from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import pymssql
def Test(*DATA):
    try:
        browser=webdriver.Ie()
        browser.maximize_window()
        browser.implicitly_wait(5)
        browser.get('http://localhost:9087')
        for data in DATA:
            print(data)
            # 元素操作
            if data[2]==1:
                if data[5]==1:
                    browser.find_element(data[3],data[4]).send_keys(data[6])
                elif data[5]==2:
                    browser.find_element(data[3],data[4]).click()
                    sleep(2)
                elif data[5]==3:
                    selement=Select(browser.find_element(data[3],data[4]))
                    selement.select_by_value(data[6])
            # 切换frame/iframe表单
            elif data[2]==2:
                if data[7]==1:
                    browser.switch_to.default_content()
                elif data[7]==2:
                    browser.switch_to.frame(data[8])
                sleep(2)
            # 切换窗口
            elif data[2]==3:
                handles=browser.window_handles
                print(handles)
                if data[9]==1:
                    browser.switch_to.window(handles[0])
                elif data[9]==2:
                    browser.switch_to.window(handles[-1])
                sleep(2)
            # 切换到弹出框
            elif data[2]==4:
                alert=browser.switch_to.alert
                if data[10]==1:
                    alert.accept()
                elif data[10]==2:
                    alert.dismiss()
                elif data[10]==3:
                    alert.send_keys(data[11])
                sleep(2)
    except Exception as E:
        print(E)
    finally:
        browser.quit()
if __name__ =='__main__':
    with pymssql.connect('127.0.0.1:1433','sa','000000','TEST') as sql:
        with sql.cursor() as cursor:
            cursor.execute('SELECT * FROM ACTIONS WHERE TESTCASE_ID =1 ')
            DATA=cursor.fetchall()
    Test(*DATA)