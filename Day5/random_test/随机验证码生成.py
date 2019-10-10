#!/usr/bin/env python
# coding:utf-8
import random
"""
Name : 随机验证码生成.py
Author  : anne
Time    : 2019-07-28 12:11
Desc:
"""
#四位数字验证码生成
# checkcode = ''
# for i in range(4):
#     current = random.randint(1,9)
#     checkcode += str(current)
# print(checkcode)
# print(type(checkcode))


#5位随机验证码即可
checkcode = ''
for i in range(5):
    current = random.randrange(0,5)
    if current == i:
        tmp = chr(random.randint(65,90))
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)
print(checkcode)


print(random.randint(1,5))
print(random.randrange(1,10))