import sys,os
path = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(path)[0]
sys.path.append(rootPath)

from 金谷集团接口自动化脚本.封装执行脚本 import Test
from 金谷集团接口自动化脚本.封装数据库返回数据方法 import Data

if __name__ == '__main__':
    with open(r'D:\自动化测试\test.txt','w') as file:
        file.write(rootPath)
    DATA=Data().data(2)
    Test().test(*DATA)