#!/usr/bin/env python
# coding:utf-8
"""
Name : 红绿灯.py
Author  : anne
Time    : 2019-08-21 15:05
Desc:
"""
import threading,time
event = threading.Event()
def lighter():
    count = 0
    event.set() #先设置绿灯
    while True:
        if count > 5 and count < 10:#改成红灯
            event.clear()#标志位清了
            print('\033[41;1mred light is on ...\033[0m')
        elif count > 10:
            event.set()#变绿灯
            count = 0
        else:
            print('\033[42;1mgreen light is on ...\033[0m')
        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():#代表绿灯
            print('[%s] running...'%name)
            time.sleep(1)
        else:
            print('[%s] sees red light ,waiting ...' %name)
            event.wait()
            print('\033[34;1m[%s] green light is on,start going ... \033[0m' %name)


light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=('宝马',))
car1.start()