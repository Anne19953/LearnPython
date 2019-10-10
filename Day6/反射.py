#!/usr/bin/env python
# coding:utf-8
"""
Name : 反射.py
Author  : anne
Time    : 2019-07-31 21:12
Desc:
"""
class Dog(object):
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print('%s is eating '%self.name)

def bark(self):
        print('%s is barking'%self.name)

d = Dog('lele')
choice = input('>>:').strip()

if hasattr(d,choice):
    func = getattr(d,choice)
    func(d)

else :

    setattr(d,choice,bark)
    func = getattr(d,choice)
    func(d)


"""
显示效果，当输入的是存在的方法，eat()或bark()时，调用方法，不是存在的方法时，调用bark


"""