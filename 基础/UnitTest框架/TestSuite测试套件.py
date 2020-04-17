import unittest

# 导入测试用例
from 基础.UnitTest框架.Case.case1 import Case1
from 基础.UnitTest框架.Case.case2 import Case2
from 基础.UnitTest框架.Case.case3 import Case3

if __name__ == '__main__':
# 实例化测试套件对象：suite=unittest.TestSuite()。
    suite=unittest.TestSuite()
# 给测试套件添加单个测试用例：suite.addTest(classname(defname))。
    suite.addTest(Case1('test1'))
# 给测试套件添加多个测试用例：suite.addTest(Iterable[classname(defname)]),参数是类名(方法名)组成的一个可迭代的对象。
    suite.addTests([Case1('test2'),Case1('test3')])
# 批量添加test开头的用例：suite.addTest(unittest.makeSuite(classname))
    suite.addTest(unittest.makeSuite(Case2))
    suite.addTest(unittest.makeSuite(Case3))
# 使用unittest.TextTestRunner的run()方法执行测试套件。
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
