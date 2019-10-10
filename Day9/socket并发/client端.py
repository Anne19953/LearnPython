#!/usr/bin/env python
# coding:utf-8
"""
Name : client端.py
Author  : anne
Time    : 2019-08-26 16:31
Desc:
"""
from socket import *
client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))

while True:
    msg = input('>>:').strip()
    if not msg:continue

    client.send(msg.encode('utf-8'))
    msg = client.recv(1024)
    print(msg.decode('utf-8'))