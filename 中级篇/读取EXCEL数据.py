import xlrd

excel=xlrd.open_workbook(r"E:\testdata\user.xls")
table=excel.sheets()[0]
print(table)
sheet=excel.sheet_by_name('user')
row=sheet.row_values(2)
col=sheet.col_values(0)
print("第三行的数据为：",row)
print("第一列的数据为：",col)
print("第三行第一列的值为：",row[0])
print("第一列第一行的值为：",col[0])
print("第二行第一列的值为：",sheet.cell(1,0).value)
print("工作表的行数为：",sheet.nrows,"工作表的列数为：",sheet.ncols)