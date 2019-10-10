#!/usr/bin/env python
# coding:utf-8
"""
Name : 多进程.py
Author  : anne
Time    : 2019-08-22 15:32
Desc:
"""
from multiprocessing import Process
import threading
import time
def thread_run():
    print(threading.get_ident())
def run(name):
    time.sleep(2)
    print('hello',name)
    t = threading.Thread(target=thread_run,)
    t.start()

if __name__ == '__main__':
    for i in range(10):
        p = Process(target = run,args=('bob %s'%i,))
        p.start()
        p.join()