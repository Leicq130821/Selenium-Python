from HTMLTestRunner import HTMLTestRunner
from datetime import datetime
import unittest

if __name__ == '__main__':
    # 定义报告文件名。
    filename=r'D:\自动化测试\%s'%datetime.now().strftime('%Y年%m月%d日 %H点%M分%S秒')+'Report.html'
    # 添加测试套件。
    suite=unittest.defaultTestLoader.discover('./Case',pattern='case*.py')
    with open(filename,'wb') as file:
        # 实例化runner，并执行测试套件。
        runner=HTMLTestRunner(stream=file,title='测试报告',description='测试内容')
        runner.run(suite)