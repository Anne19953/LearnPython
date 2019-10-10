#!/usr/bin/env python
# coding:utf-8
"""
Name : 进程池.py
Author  : anne
Time    : 2019-08-25 11:39
Desc:
"""
from multiprocessing import Process,Pool,Lock
import time,os
def Foo(i):
    time.sleep(2)
    lock.acquire()
    print('in process',os.getpid())
    lock.release()
    return i+100
def Bar(arg):
    # l.acquire()
    print('---->exec done:',arg,os.getpid())
    # l.release()

lock = Lock()
pool = Pool(3,initargs=(lock,))

print('主进程pid',os.getpid())

for i in range(5):
    pool.apply_async(func=Foo,args=(i,),callback=Bar) #回调
    # pool.apply(func=Foo,args=(i,))  #串行执行
    # pool.apply_async(func=Foo,args=(i,)) #并行执行，5个同时
print('end')
pool.close()
pool.join()

