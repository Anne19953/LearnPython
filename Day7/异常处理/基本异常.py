#!/usr/bin/env python
# coding:utf-8
"""
Name : 基本异常.py
Author  : anne
Time    : 2019-08-02 11:00
Desc:
"""
#############indecxError
dic = ['anne','songfengju']
try:
    dic[10]
except IndexError as e:
    print(e)

##############Keyvalue
dic = {'k1':'v1'}
try:
    dic['k20']
except KeyError as e:
    print(e)

###########valueError
s1 = 'hello'
try:
    int(s1)
except ValueError as e:
    print(e)


#############自定义异常
class AnneException(Exception):
    def __init__(self,msg):
        self.mssage = msg
    def __str__(self):
        return self.mssage
try:
    raise AnneException("我的异常")
except AnneException as e:
    print(e)