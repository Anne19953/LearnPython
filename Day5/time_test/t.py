#!/usr/bin/env python
# coding:utf-8
"""
Name : t.py
Author  : anne
Time    : 2019-07-27 16:54
Desc:
"""
import time
#结构化时间
x = time.localtime()
print(x)
#想知道具体的年
print(x.tm_year)

#格式化的字符串
t = time.strftime('%Y-%m-%d %H:%m:%s',x)
print(t)

#时间戳
print(time.time())

#将结构化时间转为时间戳
print(time.mktime(x))


#将结构化时间转为格式化的字符串
print(time.asctime(x))

#将时间戳转为格式化的字符串
print(time.ctime(time.time()))
