import pymssql

# 实例化数据库连接对象。
sql=pymssql.connect('127.0.0.1:1433','sa','000000','intrust')
# 实例化游标。
cursor=sql.cursor()
# 游标执行sql语句。
cursor.execute('SELECT LOGIN_USER,PASSWORD FROM TOPERATOR WHERE OP_CODE<1000')
# 读取数据。
data=cursor.fetchall()
print(data)
cursor.close()
sql.close()