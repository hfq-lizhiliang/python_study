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
    while n > 0:
        print 'T-minus', n
        n -= 1
        time.sleep(1)


from threading import Thread

# 创建一个线程并启用
# t=Thread(target=countdown, args=(10,))
# t.start()

"""
可以查询一个线程的状态，看它是否还在执行
"""
# if t.is_alive:
#     print 'Still running'
# else:
#     print 'Complieted'

'''
可以将一个线程加入到当前线程中，并等待结束
'''
# t=Thread(target=countdown, args=(10,))
# t.start()
# t.join() # 当线程t接入后，当前线程才会继续执行下面

'''
Python解释器直到所有线程都终止前仍保持运行。对于
需要长时间运行的线程或者需要一直运行的后台任务，你应当考虑使用后台线程
'''

# t = Thread(target=countdown, args=(10,))
# # 后台运行
# t.daemon=True
# t.start()

'''
后台运行无法等待，不过会在主线程销毁时也结束.
你无法结束一个线程，无法给它发送信号，无法调整它的调度，也无法执行其他高级操作。如果需要这些特性，
你需要自己添加。比如说，如果你需要终止线程，那么这个线程必须通过编程在某个特定点轮询来退出。你可以像下边这样把线程放入一个类中

如果执行一些像I/O这样的阻塞操作，那么通过轮训来终止线程将使得线程之间的协调变得非常棘手。利用超时循环来小心操作线程。
'''


class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print 'T-minus', n
            n -= 1
            time.sleep(5)


# c=CountdownTask()
# t=Thread(target=c.run, args=(10,))
# t.start()
# c.terminate()
# t.join()


'''
有时你会看到下边这种通过继承 Thread 类来实现的线程
'''


class CountdownThread(Thread):
    def __init__(self, n):
        super(CountdownThread, self).__init__()
        self.n = 0

    def run(self):
        while self.n > 0:
            print 'T-minus', self.n
            self.n -= 1
            time.sleep(5)


# c = CountdownThread(5)
# c.start()

'''
尽管这样也可以工作，但这使得你的代码依赖于 threading 库，所以你的这些代码只能在线程上下文中使用。上文所写的那些代码、函数都是与 threading 库无关的，这样就使得这些代码可以被用在其他的上下文中，可能与线程有关，也可能与线程无关。比如，你可以通过 multiprocessing 模块在一个单独的进程中执行你的代码：
'''


'''
在脚本中使用 multiprocessing 时，需要在__name__ == '__main__'下执行，否则会报错
'''
import multiprocessing

if __name__ == '__main__':
    c = CountdownTask()
    p = multiprocessing.Process(target=c.run, args=(5,))
    print p.is_alive()
    p.start()
