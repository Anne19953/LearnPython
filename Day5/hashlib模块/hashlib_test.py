#!/usr/bin/env python
# coding:utf-8
"""
Name : hashlib_test.py
Author  : anne
Time    : 2019-07-28 18:57
Desc:
"""
import hashlib
import hmac
m = hashlib.md5()

m.update(b'hello')
m.update(b"it's me")
print(type(m))
print(m.digest())


m1 = hashlib.md5()
m1.update(b"helloit's me")
print(m1.digest())
print(m1.hexdigest())

#中文格式
m2 = hashlib.md5()
m2.update('你好'.encode(encoding='utf-8'))
print(m2.digest())


#hmac加密
h = hmac.new('你好'.encode(encoding='utf-8'))
print(h.hexdigest())







