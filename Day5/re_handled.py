#!/usr/bin/env python
# coding:utf-8
"""
Name : re_handled.py
Author  : anne
Time    : 2019-07-29 16:59
Desc:
"""
import re
import functools
#处理一些特殊的减号运算
def minus_operator_handler(formula):
    minis_operators = re.split('-',formula)
    calc_list = re.findall('[0-9]',formula)