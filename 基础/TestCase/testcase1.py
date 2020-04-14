import unittest

class number1(unittest.TestCase):
    def test1(self):
        print('第一个用例被执行')
    def test2(self):
        print('第一个用例又被执行')
    def test3(self):
        print('再一次执行第一个用例')
if __name__ == '__main__':
    unittest.main()
