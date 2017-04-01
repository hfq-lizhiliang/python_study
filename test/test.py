#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/1 15:57
# @Author  : zhiliang
# @Site    : 
# @File    : test.py
# @Software: PyCharm


# import multiprocessing
# import time
#
#
# class CountdownTask:
#     def __init__(self):
#         self._running = True
#
#     def terminate(self):
#         self._running = False
#
#     def run(self, n):
#         while self._running and n > 0:
#             print 'T-minus', n
#             n -= 1
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     c = CountdownTask()
#     p = multiprocessing.Process(target=c.run, args=(5,))
#     print p.is_alive()
#     p.start()
#     a=2
#     a^=3
#     print a



# import threading
# import time
#
# class PeriodicTimer:
#     def __init__(self, interval):
#         self._interval = interval
#         self._flag = 0
#         self._cv = threading.Condition()
#
#     def start(self):
#         t = threading.Thread(target=self.run)
#         t.daemon = True
#
#         t.start()
#
#     def run(self):
#         '''
#         Run the timer and notify waiting threads after each interval
#         '''
#         while True:
#             time.sleep(self._interval)
#             with self._cv:
#                  self._flag ^= 1 # 位异或运算
#                  self._cv.notify_all()
#
#     def wait_for_tick(self):
#         '''
#         Wait for the next tick of the timer
#         '''
#         with self._cv:
#             last_flag = self._flag
#             # print "last_flag=%s,_flag=%s" % (last_flag, self._flag)
#             while last_flag == self._flag:
#                 self._cv.wait()
#
# # Example use of the timer
# ptimer = PeriodicTimer(5)
# ptimer.start()
#
# # Two threads that synchronize on the timer
# def countdown(nticks):
#     while nticks > 0:
#         ptimer.wait_for_tick()
#         print 'T-minus=%s   ' % nticks
#         nticks -= 1
#
# def countup(last):
#     n = 0
#     while n < last:
#         ptimer.wait_for_tick()
#         print 'Counting=%s   '% n
#         n += 1
#
# threading.Thread(target=countdown, args=(10,)).start()
# threading.Thread(target=countup, args=(5,)).start()



#Wroker thread
import threading


def worker(n, sema):
    #Wait to be singnaled
    sema.acquire()
    #Do some work
    print 'Working',n

# Create some threads
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t=threading.Thread(target=worker, args=(n, sema))
    t.start()