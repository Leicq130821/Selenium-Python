import unittest

class Case1(unittest.TestCase):
    def test1(self):
        print('用例1的测试1被执行')
    def test2(self):
        print('用例1的测试2被执行')
    def test3(self):
        print('用例1的测试3被执行')
if __name__ == '__main__':
    unittest.main()