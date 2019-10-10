#!/usr/bin/env python
# coding:utf-8
"""
Name : client.py
Author  : anne
Time    : 2019-08-27 11:20
Desc:
"""
# import socket
# sk = socket.socket()
# sk.connect(('127.0.0.1',9904))
#
# while 1:
#     inp = input('>>').strip()
#     sk.send(inp.encode('utf-8'))
#     # data = sk.recv(1024)
#     # print(data.decode('utf-8'))

#***********************client.py

import socket
sk=socket.socket()
sk.connect(('127.0.0.1',8801))

while True:
    inp=input(">>>>")
    sk.sendall(bytes(inp,"utf8"))
    data=sk.recv(1024)
    print(str(data,'utf8'))