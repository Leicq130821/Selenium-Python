from HTMLTestRunner import HTMLTestRunner
import unittest
from datetime import datetime

if __name__ == '__main__':
    # 添加测试套件
    suite=unittest.defaultTestLoader.discover('./Case',pattern='case*.py')
    #定义报告的文件目录
    file_name=r'D:\自动化测试\%sReport.html'%datetime.now().strftime('%Y年%m月%d日 %H点%M分%S秒')
    #写入报告
    with open(file_name,"wb") as f:
        runner=HTMLTestRunner(stream=f,title='测试报告',description='测试内容')
        runner.run(suite)