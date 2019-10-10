#!/usr/bin/env python
# coding:utf-8
"""
Name : dog.py
Author  : anne
Time    : 2019-07-29 20:20
Desc:
"""
class Dog:
    def __init__(self,name):
        self.name = name
    def bulk(self):
        print('%s wangwangwang!' %self.name)


d1 = Dog('大举')
d2 = Dog('anne')
d3 = Dog('燕飞')

d1.bulk()
d2.bulk()
d3.bulk()

