#!/usr/bin/env python
# coding:utf-8
"""
Name : 守护线程.py
Author  : anne
Time    : 2019-08-31 17:20
Desc:
"""
from threading import Thread
import time
def foo():
    print(123)
    time.sleep(3)
    print("end123")

def bar():
    print(456)
    time.sleep(1)
    print("end456")


t1=Thread(target=foo)
t2=Thread(target=bar)

t1.daemon=True
t1.start()
t2.start()
print("main-------")