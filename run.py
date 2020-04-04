# coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
from libs.ShareModules import getTestSuite
from libs.ShareModules import getTestCases
import os,time

def get_test_suite():
    try:
        discover = unittest.defaultTestLoader.discover(r'./scripts', pattern='*_test.py')
        suite_m = getTestSuite(discover)
        suite_c = getTestCases(suite_m)
        return suite_c
    except:
        print('开始执行用例失败')

if __name__ == '__main__':

    discover = get_test_suite()
    current_time = time.strftime('%Y%m%d_%H%M%S')
    filedir = './report/' + current_time + '.html'
    fp = open(filedir, 'wb+')
    hrunner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=r'测试报告', description='描述')
    hrunner.run(discover)
    fp.close()


    # runner = unittest.TextTestRunner()
    # runner.run(get_test_suite())






    pass