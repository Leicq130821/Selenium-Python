import unittest

class Case1(unittest.TestCase):
    def test1(self):
        print('用例1的第1个方法被执行！')
    def test2(self):
        print('用例1的第2个方法被执行！')
    def test3(self):
        print('用例1的第3个方法被执行！')
if __name__ == '__main__':
    unittest.main()
