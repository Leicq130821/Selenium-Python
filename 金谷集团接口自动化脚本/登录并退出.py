from 金谷集团接口自动化脚本.封装执行脚本 import Test
from 金谷集团接口自动化脚本.封装数据库返回数据方法 import Data

if __name__ == '__main__':
    DATA=Data().data(2)
    Test().test(*DATA)