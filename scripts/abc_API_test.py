import unittest

class abcTest(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_abc_01(self):
        print('测试模块：2   测试用例：abc_01')
    def test_abc_02(self):
        print('测试模块：2   测试用例：abc_02')
    def test_abc_03(self):
        print('测试模块：2   测试用例：abc_03')

if __name__ == '__main__':
    unittest.main(verbosity=3)