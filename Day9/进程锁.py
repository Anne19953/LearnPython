#!/usr/bin/env python
# coding:utf-8
"""
Name : 进程锁.py
Author  : anne
Time    : 2019-08-25 12:10
Desc:存在的意义是打印很多进程时，不乱，屏幕是共享的
"""
from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    print('hello world', i)
    l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(1000):
        Process(target=f, args=(lock, num)).start()
