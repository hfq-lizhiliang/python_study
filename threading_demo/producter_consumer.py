# coding: utf-8

# #多线程实现生产者、消费者

# In[1]:

import time, threading


# 线程代码
class TaskThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        print 'thread %s is running...' % self.getName()
        for i in range(6):
            print 'thread %s >>> %s' % (self.getName(), i)
            time.sleep(1)
        print 'thread %s finished' % self.getName()


taskthread = TaskThread('TaskThread')
taskthread.start()
taskthread.join()

# #在上面的简单的Python线程后，下面我们实现一个生产者消费者模式

# In[ ]:

from Queue import Queue
import random, threading, time


# 生产者
class Producer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            print '%s is producing %d to the queue' % (self.getName(), i)
            self.data.put(i)
            time.sleep(random.randrange(10) / 5)
        print '%s finished ' % self.getName()


# 消费者类
class Consumer(threading.Thread):
    def __init__(self, name, queue):
        threading.Thread.__init__(self, name=name)
        self.data = queue

    def run(self):
        for i in range(5):
            val = self.data.get()
            print '%s is consuming, %d in the queue id constumer' % (self.getName(), val)
            time.sleep(random.randrange(10))
        print '%s finished' % self.getName()


def main():
    queue = Queue()
    producter = Producer('producer', queue)
    consumer = Consumer('Customer', queue)
    producter.start()
    consumer.start()

    producter.join()
    consumer.join()
    print 'All threads finished'


main()



# producer is producing 0 to the queue
# Customer is consuming, 0 in the queue id constumer
# producer finished 
# producer is producing 1 to the queue
# producer finished 
# producer is producing 2 to the queue
# producer finished 
# producer is producing 3 to the queue
# producer finished 
# producer is producing 4 to the queue
# producer finished 
# Customer is consuming, 1 in the queue id constumer
# Customer is consuming, 2 in the queue id constumer
# Customer is consuming, 3 in the queue id constumer
# Customer is consuming, 4 in the queue id constumer
# Customer finished
# All threads finished

# 因为多线程是抢占式执行的，所以打印出的运行结果不一定和上面的完全一致。

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:
