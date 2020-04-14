import unittest

class TEST(unittest.TestCase):
    def test1(self):
        print('test1被执行')
    def test2(self):
        print('test2被执行')
    def test3(self):
        print('test3被执行')
if __name__ == '__main__':
    unittest.main()