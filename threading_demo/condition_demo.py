
# coding: utf-8

# #### 线程同步（Event对象）

# In[8]:

from threading import Thread, Event
import time


# In[9]:

def countdown(n, started_evt):
    print 'countdown starting'
    started_evt.set()
    while n > 0:
        print 'T-minut', n
        n-=1
        time.sleep(5)


# In[20]:

started_evt = Event() # python3没有后面的括号
print 'Launvhing countdown'
t=Thread(target=countdown, args=(5, started_evt))
t.start()
# Wait for the thread to start
started_evt.wait()
print 'countdown is running'


# 当你执行上面这段代码，“countdown is running” 总是显示在 “countdown starting” 之后显示。这是由于使用 event 来协调线程，使得主线程要等到 countdown() 函数输出启动信息后，才能继续执行。

# #讨论

# event 对象最好单次使用，就是说，你创建一个 event 对象，让某个线程等待这个对象，一旦这个对象被设置为真，你就应该丢弃它。尽管可以通过 clear() 方法来重置 event 对象，但是很难确保安全地清理 event 对象并对它重新赋值。很可能会发生错过事件、死锁或者其他问题（特别是，你无法保证重置 event 对象的代码会在线程再次等待这个 event 对象之前执行）。如果一个线程需要不停地重复使用 event 对象，你最好使用 Condition 对象来代替。下面的代码使用 Condition 对象实现了一个周期定时器，每当定时器超时的时候，其他线程都可以监测到：

# In[36]:

import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True

        t.start()

    def run(self):
        '''
        Run the timer and notify waiting threads after each interval
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                 self._flag ^= 1 # 位异或运算
                 self._cv.notify_all()

    def wait_for_tick(self):
        '''
        Wait for the next tick of the timer
        '''
        with self._cv:
            last_flag = self._flag
#             print "last_flag=%s,_flag=%s" % (last_flag, self._flag)
            while last_flag == self._flag:
                self._cv.wait()

# Example use of the timer
ptimer = PeriodicTimer(1)
ptimer.start()

# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1

def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n += 1

threading.Thread(target=countdown, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()


# ![](http://jbcdn2.b0.upaiyun.com/2015/11/e1c72bee29347377e5e580e49fa8607e.png)

# In[37]:


#---- Condition
#---- 捉迷藏的游戏
import threading, time
class Hider(threading.Thread):
    def __init__(self, cond, name):
        super(Hider, self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        time.sleep(1) #确保先运行Seeker中的方法
        self.cond.acquire() #b
        print self.name + ': 我已经把眼睛蒙上了'
        self.cond.notify()
        self.cond.wait() #c
                         #f
        print self.name + ': 我找到你了 ~_~'
        self.cond.notify()
        self.cond.release()
                            #g
        print self.name + ': 我赢了'   #h
class Seeker(threading.Thread):
    def __init__(self, cond, name):
        super(Seeker, self).__init__()
        self.cond = cond
        self.name = name
    def run(self):
        self.cond.acquire()
        self.cond.wait()    #a    #释放对琐的占用，同时线程挂起在这里，直到被notify并重新占有琐。
                            #d
        print self.name + ': 我已经藏好了，你快来找我吧'
        self.cond.notify()
        self.cond.wait()    #e
                            #h
        self.cond.release()
        print self.name + ': 被你找到了，哎~~~'
cond = threading.Condition()
seeker = Seeker(cond, 'seeker')
hider = Hider(cond, 'hider')
seeker.start()
hider.start()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



