#!/usr/bin/env python
# coding:utf-8
"""
Name : tset.py
Author  : anne
Time    : 2019-08-02 20:06
Desc:
"""


# lib = __import__('import_lib.aa')
# obj = lib.aa.C()
# print(obj.name)

########################################

import importlib
lib = importlib.import_module('import_lib.aa')
print(lib.C().name)


