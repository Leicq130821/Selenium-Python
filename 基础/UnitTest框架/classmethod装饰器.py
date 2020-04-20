import unittest

class Test(unittest.TestCase):
    @classmethod
    # 前置函数。
    def setUpClass(cls):
        print('全部测试案例执行前执行！')
    @classmethod
    # 后置函数。
    def tearDownClass(cls):
        print('全部测试案例执行完毕后再执行！')
    def test1(self):
        print('执行测试1')
    def test2(self):
        print('执行测试2')
    def test3(self):
        print('执行测试3')
if __name__ =='__main__':
    unittest.main()