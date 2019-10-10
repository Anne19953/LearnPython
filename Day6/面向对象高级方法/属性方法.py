#!/usr/bin/env python
# coding:utf-8
"""
Name : 属性方法.py
Author  : anne
Time    : 2019-07-31 15:33
Desc:
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print('%s is eating' % self.name)


d = Dog('anne')
# d.eat()   这样调用会报错
d.eat  # eat此时已经变成一个静态属性了，不是方法了，想调用已经不需要加()号了
