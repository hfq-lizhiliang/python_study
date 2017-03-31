#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/31 23:00
# @Author  : zhiliang
# @Site    : 
# @File    : thread_test.py.py
# @Software: PyCharm

'''
threading 库可以在单独的线程中执行任何的在python中可以调用的对象，你可以创建一个Thread对象将
你要执行的对象以target参数的形式提供给对象
'''

import time
def countdown(n):
    while n>0:
        print 'T-minus', n
        n-=1
        time.sleep(1)
from threading import Thread
# 创建一个线程并启用
t=Thread(target=countdown, args=(10,))
t.start()

"""
可以查询一个线程的状态，看它是否还在执行
"""
if t.is_alive:
    print 'Still running'
else:
    print 'Complieted'

'''
可以将一个线程加入到当前线程中，并等待结束
'''
t=Thread(target=countdown, args=(10,))
t.start()
t.join() # 当线程t接入后，当前线程才会继续执行下面

'''
Python解释器直到所有线程都终止前仍保持运行。对于
需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程
'''

t = Thread(target=countdown, args=(10,))
# 后台运行
t.daemon=True
t.start()

'''
后台运行无法等待，不过会在主线程销毁时也结束.
你无法结束一个线程，无法给它发送信号，无法调整它的调度，也无法执行其他高级操作。如果需要这些特性，
你需要自己添加。比如说，如果你需要终止线程，那么这个线程必须通过编程在某个特定点轮询来退出。你可以像下边这样把线程放入一个类中
'''

class CountdownTask:
    def __init__(self):
        self._running = True
    def terminate(self):
        self._running = False
    def run(self, n):
        while self._running and n > 0:
            print 'T-minus', n
            n-=1
            time.sleep(5)

c=CountdownTask()
t=Thread(target=c.run, args=(10,))
t.start()
c.terminate()
t.join()
