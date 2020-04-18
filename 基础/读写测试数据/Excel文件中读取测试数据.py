import xlrd

# 实例化Excel对象。
excel=xlrd.open_workbook(r'D:\自动化测试\data.xlsx')
# 通过索引获取sheet。
sheet=excel.sheets()[0]
sheet=excel.sheet_by_index(0)
# 通过名称获取sheet。
sheet=excel.sheet_by_name('Sheet1')
# 获取sheet的行数。
print(sheet.nrows)
# 获取sheet的列数。
print(sheet.ncols)
# 获取某一行数据。
row=sheet.row(1)
print(row)
# 获取某一列数据。
col=sheet.col(0)
print(col)
# 获取某一行的某列数据。
print(row[1])
# 获取某一列的某行数据。
print(col[0])
# 通过sheet获取某行某列数据。
print(sheet.cell(2,1).value)