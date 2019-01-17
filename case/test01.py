#coding:utf-8
import unittest
import time

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("开始测试")
    def tearDown(self):
        print("测试结束")
    def test01(self):
        '''测试0201'''
        print("执行测试用例1")
    def test02(self):
        '''测试0202'''
        print("执行测试用例02")

if __name__=="__main__":
    unittest.main()