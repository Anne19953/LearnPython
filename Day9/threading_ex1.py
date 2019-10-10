#!/usr/bin/env python
# coding:utf-8
"""
Name : threading_ex1.py
Author  : anne
Time    : 2019-08-19 14:25
Desc:简单的多线程实现
"""

import threading
import time
# def run(n):
#     print('task',n)
#     time.sleep(2)
#
# t1 = threading.Thread(target=run,args=('t1',))
# t2 = threading.Thread(target=run,args=('t2',))

#多线程模拟
# t1.start()
# t2.start()

#单线程
# run('t1')
# run('t2')


def run(n):
    print('task',n)
    time.sleep(2)
    print('task done',n)


start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s' %i,))
    t.start()
    #这样每个线程都能执行完毕后才执行下一个线程,这种每个线程都需要花2S
    #t.join()
    t_objs.append(t)

for t in t_objs:
    t.join()


print('cost:',time.time() - start_time)



