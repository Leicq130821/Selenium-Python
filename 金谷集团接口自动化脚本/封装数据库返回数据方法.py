import pymssql

class Data():
    def data(self,TESTCASE_ID):
        with pymssql.connect('127.0.0.1:1433','sa','000000','TEST') as sql:
            with sql.cursor() as cursor:
                cursor.execute('SELECT * FROM ACTIONS WHERE TESTCASE_ID = %s'%TESTCASE_ID)
                datalist=cursor.fetchall()
        return datalist