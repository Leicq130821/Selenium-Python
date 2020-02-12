import unittest

if __name__ == '__main__':
    suite=unittest.defaultTestLoader.discover("./TestCase",pattern="test*.py")
    runner=unittest.TextTestRunner()
    runner.run(suite)