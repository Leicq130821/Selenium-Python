from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest

if __name__ == '__main__':
    filename=r'D:\自动化测试\%s'%datetime.now().strftime('%Y年%m月%d日 %H点%M分%S秒')+'Report.html'
    suite=unittest.defaultTestLoader.discover('./Case',pattern='case*.py')
    with open(filename,'wb') as file:
        runner=HTMLTestRunner(stream=file,title='测试报告',description='测试内容')
        runner.run(suite)