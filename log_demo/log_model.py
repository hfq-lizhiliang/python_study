#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 16:10
# @Author  : zhiliang
# @Site    : 
# @File    : log_model.py
# @Software: PyCharm

# import logging
# from logging.config import fileConfig
#
# logging.config.fileConfig('logging.conf')
#
# #create logger
# logger = logging.getLogger('simpleExample')
#
# # application code
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('wran message')
# logger.error('error message')
# logger.critical('critical message')


from os import path
import logging
from logging.config import fileConfig
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

path1 = "path:>>>   %s "
path2 = "path.abspath(__file__):>>>   %s "
path3 = "path.dirname(path.abspath(__file__)):>>>   %s "
path4 = "path.join(path.dirname(path.abspath(__file__)), 'logging.conf'):>>>   %s"

print path1 % path
print path2 % path.abspath(__file__)
print path3 % path.dirname(path.abspath(__file__))
print path4 % path.join(path.dirname(path.abspath(__file__)), 'logging.conf')

'''
打印路径：
path:>>>   <module 'ntpath' from 'C:\Python27\lib\ntpath.pyc'>
path.abspath(__file__):>>>   F:\lizhiliang-hzf\python_study\log_demo\log_model.py
path.dirname(path.abspath(__file__)):>>>   F:\lizhiliang-hzf\python_study\log_demo
path.join(path.dirname(path.abspath(__file__)), 'logging.conf'):>>>   F:\lizhiliang-hzf\python_study\log_demo\logging.conf
'''


logging.config.fileConfig(log_file_path)

#create logger
logger = logging.getLogger('simpleExample')

# application code
logger.debug('debug message')
logger.info('info message')
logger.warn('wran message')
logger.error('error message')
logger.critical('critical message')


