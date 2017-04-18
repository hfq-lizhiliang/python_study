#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/18 15:55
# @Author  : zhiliang
# @Site    : 
# @File    : demo2.py
# @Software: PyCharm


# import logging
# logging.warning('%s before you %s', 'Look', 'leap!')


import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This message should appear on the console')
# logging.info('So should this')
# logging.warning('And this, too')
'''
DEBUG:root:This message should appear on the console
INFO:root:So should this
WARNING:root:And this, too
'''
#自定义输出格式
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')