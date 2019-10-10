#!/usr/bin/env python
# coding:utf-8
"""
Name : 静态方法.py
Author  : anne
Time    : 2019-07-31 14:28
Desc:
"""


class Dog(object):
    def __init__(self, name):
        self.name = name

    @staticmethod
    # def eat(self):
    #     print('%s is eating' % self.name)
    def eat():  # eat不能通过self.调用实例中的其他变量
        print(' is eating')


d = Dog('anne')
# d.eat(d)   #这种情况下是可以传参进去的
d.eat()  # 不传参数
