#!/usr/bin/env python
# coding:utf-8
"""
Name : shelve_test.py
Author  : anne
Time    : 2019-07-28 15:56
Desc:
"""

import shelve


#写入文件
# d = shelve.open('shelve_test')
# info = {'age':22,'name':'anne'}
# name = ['alex','rain','test']

# d['name'] = name
# d ['info'] = info

#读取文件内容
d = shelve.open('shelve_test')
print(d.get('name'))
print(d.get('info'))

d.close()