from HTMLTestRunner import HTMLTestRunner
import unittest
import time

suite=unittest.defaultTestLoader.discover("./Case",pattern="test*.py")

if __name__ == '__main__':
    #定义报告的文件目录
    dir_path="./Report/"
    nowtime=time.strftime("%Y_%m_%d_%H_%M_%S")
    file_name=dir_path+nowtime+"Report.html"
    #写入报告
    with open(file_name,"wb") as f:
        runner=HTMLTestRunner(stream=f,title='测试报告',description='说明')
        runner.run(suite)