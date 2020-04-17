import unittest

# 测试类必须继承unittest.TestCase类。
class Test(unittest.TestCase):
# 测试方法必须以test开头。
    def testcase1(self):
        print('测试用例1被执行！')
    def testcase2(self):
        print('测试用例2被执行！')
    def testcase3(self):
        print('测试用例3被执行！')
if __name__ == '__main__':
# 通过函数unittest.main()来运行test开头的方法。
    unittest.main()