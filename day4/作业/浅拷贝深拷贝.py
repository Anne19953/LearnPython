#!/usr/bin/env python
# coding:utf-8
"""
Name : 浅拷贝深拷贝.py
Author  : anne
Time    : 2019-07-26 16:24
Desc:
"""

#浅拷贝 B复制A，修改A，B跟着改变
import copy
person = ['name',['saving',100]]
'''
p1 = copy.copy(person)
p2 = person[:]
p3 = list(person)

'''
p1 = person[:]
p2 = person[:]

p1[0] = 'anne'
p2[0] = 'songfengju'

p1[1][1] = 50

print(p1)
print(p2)