#!/usr/bin/env python
# coding:utf-8
"""
Name : shutil_test.py
Author  : anne
Time    : 2019-07-28 15:13
Desc:
"""
import shutil
# f1 = open('测试1',encoding='utf-8')
# f2 = open('测试2','w',encoding='utf-8')
# shutil.copyfileobj(f1,f2)

#拷贝文件内容
# shutil.copyfile('测试1','测试3')

#拷贝状态信息，测试3文件需要原先就存在
shutil.copystate('测试1','测试3')

#拷贝目录
shutil.copytree()

