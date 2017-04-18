#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 15:51
# @Author  : zhiliang
# @Site    : 
# @File    : demo1.py
# @Software: PyCharm

'''
日志官方地址
https://docs.python.org/2.7/howto/logging.html

'''


# myapp.py
import logging
import mylib

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()
