#!/usr/bin/env python
# coding:utf-8
"""
Name : 生成者消费者.py
Author  : anne
Time    : 2019-08-22 10:27
Desc:主要使用了队列，生产者--->队列--->消费者
"""
import threading
import time
import queue
# q = queue.Queue(maxsize=10)
# def Producer(name):
#     count = 0
#     while True:
#         q.put('骨头 %s'%count)
#         print('生产了骨头 %s'%count)
#         count += 1
#         time.sleep(0.5)
#
# def Consumer(name):
#     while True:
#         print('[%s] 取到 [%s] 并且吃了它。。。'%(name,q.get()))
#         time.sleep(2)
#
# p = threading.Thread(target=Producer,args=('Anne',))
# c = threading.Thread(target=Consumer,args=('宋风举',))
# c1 = threading.Thread(target=Consumer,args=('哈哈',))
#
# p.start()
# c.start()
# c1.start()

from multiprocessing import Process,Queue
import time,random,os
def consumer(q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    c1.start()
    print('主')