import unittest

if __name__ == '__main__':
# 通过指定路径下的指定文件搜索test开头的方法。
    suite=unittest.defaultTestLoader.discover('./Case',pattern='case*.py')
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)