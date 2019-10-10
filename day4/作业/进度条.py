#!/usr/bin/env python
# coding:utf-8
"""
Name : 进度条.py
Author  : anne
Time    : 2019-07-26 21:08
Desc:
"""
import sys,time
for i in range(20):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)