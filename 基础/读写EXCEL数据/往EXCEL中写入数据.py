import xlsxwriter
import xlwt

excel=xlsxwriter.Workbook(r'E:\testdata\tes1.xls')
sheet=excel.add_worksheet('TEST')
sheet.write_string(0,0,'nanme')
sheet.write_string('B2','nanme')
sheet.set_column('A:E',30)
excel.close()

wenjian=xlwt.Workbook(encoding='utf-8')
table=wenjian.add_sheet('TEST')
table.write(1,2,label='name')
wenjian.save(r'E:\testdata\tes2.xls')