from time import sleep
import pymysql
import sys
from saveresult import SaveResult
import xlrd
class Login:
    def login_sql(driver,user):
        for data in user:
            print(data)
            driver.find_element_by_id('account').clear()
            driver.find_element_by_id('account').send_keys(data['username'])
            driver.find_element_by_name('password').clear()
            driver.find_element_by_name('password').send_keys(data['password'])
            driver.find_element_by_id('submit').click()
            sleep(5)
            username = driver.find_element_by_class_name('dropdown-toggle').text
            mysql = pymysql.connect(host='localhost', port=3306, user='root',password='000000', db='zentaoep',charset='utf8')
            user= data['username']
            sql = "select realname from zt_user where account='%s'"%user
            cursor = mysql.cursor()
            cursor.execute(sql)
            loginname = cursor.fetchone()
            name=''.join(loginname)
            if username==name:
                SaveResult.savesuccess('登陆成功，账号为：%s'%name)
            else:
                SaveResult.savefail('登陆失败，账号为：%s' % name)
                sys.exit()
            driver.find_element_by_link_text(name).click()
            driver.find_element_by_link_text('签退').click()
            sleep(5)
            url=driver.current_url
            if url=='http://127.0.0.1/biz/user-login.html':
                SaveResult.savesuccess('退出成功，账号为：%s' % name)
            else:
                SaveResult.savefail('退出失败，账号为：%s' % name)
                sys.exit()
    def login_excel(driver, excel):
        excel=xlrd.open_workbook(excel)
        sheet=excel.sheet_by_name('user')
        user=sheet.col_values(0)
        password=sheet.col_values(1)
        username=sheet.col_values(2)
        num=sheet.nrows
        i=1
        while i<num:
            driver.find_element_by_id('account').clear()
            driver.find_element_by_id('account').send_keys(user[i])
            driver.find_element_by_name('password').clear()
            driver.find_element_by_name('password').send_keys(password[i])
            driver.find_element_by_id('submit').click()
            sleep(5)
            driver.find_element_by_link_text(username[i]).click()
            driver.find_element_by_link_text('签退').click()
            sleep(5)
            i+=1