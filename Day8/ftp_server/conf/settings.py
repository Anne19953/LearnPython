#!/usr/bin/env python
# coding:utf-8
"""
Name : settings.py
Author  : anne
Time    : 2019-08-06 15:23
Desc:
"""
import os
#ftp_server所在的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IP = '127.0.0.1'
PORT = 8080
ACCOUNT_PATH = os.path.join(BASE_DIR,'conf','accounts.cfg')

