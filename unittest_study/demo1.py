#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 13:53
# @Author  : zhiliang
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

import unittest


def fun(x):
    return x + 1


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

if __name__ == '__main__':
    unittest.main()