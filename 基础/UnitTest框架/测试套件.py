import unittest
from ..TestCase.testcase1 import number1
from ..TestCase.testcase2 import number2
from ..TestCase.testcase3 import number3

if __name__ == '__main__':
    suite=unittest.TestSuite()
    # suite.addTest(number1('test1'))
    # suite.addTest(number2('test2'))
    # suite.addTest(number3('test3'))
    # suite=unittest.defaultTestLoader.discover("./TestCase",pattern="test*.py")
    suite.addTest(unittest.makeSuite(number1))
    suite.addTest(unittest.makeSuite(number2))
    suite.addTest(unittest.makeSuite(number3))
    runner=unittest.TextTestRunner()
    runner.run(suite)
if __name__ == '__main__':
    unittest.main()