#!/usr/bin/env python
# coding:utf-8
"""
Name : 类方法.py
Author  : anne
Time    : 2019-07-31 15:21
Desc:
"""


class Dog(object):
    name = '我是类变量'

    def __init__(self, name):
        self.name = name

    @classmethod  # 类方法只能访问类变量不能访问实例变量
    def eat(self):
        print('%s is eating' % self.name)


d = Dog('anne')
d.eat()  # 我是类变量 is eating
