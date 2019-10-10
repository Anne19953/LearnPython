#!/usr/bin/env python
# coding:utf-8
"""
Name : ftp_server.py
Author  : anne
Time    : 2019-08-06 15:24
Desc:
"""
import os,sys
PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)

from core import main
if __name__ == '__main__':
    main.ArgvHandler()