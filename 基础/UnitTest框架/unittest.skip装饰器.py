import unittest

class Test(unittest.TestCase):
    def testcase1(self):
        print('测试用例1被执行！')
    # 屏蔽用例的执行
    @unittest.skip('先屏蔽一下')
    def testcase2(self):
        print('测试用例2被执行！')
    def testcase3(self):
        print('测试用例3被执行！')
if __name__ == '__main__':
    unittest.main()