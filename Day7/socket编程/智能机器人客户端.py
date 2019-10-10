#!/usr/bin/env python
# coding:utf-8
"""
Name : 智能机器人客户端.py
Author  : anne
Time    : 2019-08-02 17:20
Desc:
"""
import socket
client = socket.socket()
client.connect(('127.0.0.1',8888))
client.settimeout(5)

while True:
    data = client.recv(1024)
    print('receive',data.decode())
    inp = input('please input:')
    client.sendall(inp.encode('utf-8'))
    if inp == 'exit':
        break

client.close()