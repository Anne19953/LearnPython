#!/usr/bin/env python
# coding:utf-8
"""
Name : 多重继承.py
Author  : anne
Time    : 2019-07-30 19:51
Desc:
"""
#多重继承时执行父类构造函数的顺序
class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print('B')
class C(A):
    def __init__(self):
        print('C')
class D(B,C):
    #先找B的构造函数，B中没有的时候找C的构造函数，C中也，没有时找A
    # def __init__(self):
    #     print(D)
    pass

d1 = D()