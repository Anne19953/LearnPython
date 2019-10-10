#!/usr/bin/env python
# coding:utf-8
"""
Name : 守护进程.py
Author  : anne
Time    : 2019-08-26 17:03
Desc:
"""
#主进程代码运行完毕,守护进程就会结束
from multiprocessing import Process
from threading import Thread
import time
def foo():
    print(123)
    time.sleep(1)
    print("end123")

def bar():
    print(456)
    time.sleep(3)
    print("end456")


p1=Process(target=foo)
p2=Process(target=bar)

p1.daemon=True   #将p1设置为守护进程
p1.start()
p2.start()
time.sleep(0.1)
print("main-------") #打印该行则主进程代码结束,则守护进程p1应该被终止,
# 可能会有p1任务执行的打印信息123,因为主进程打印main----时,p1也执行了,但是随即被终止