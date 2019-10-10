#!/usr/bin/env python
# coding:utf-8
"""
Name : socket_client.py
Author  : anne
Time    : 2019-08-05 14:50
Desc:
"""
import socket
client = socket.socket()
client.connect(('127.0.0.1',9999))
while True:
    msg = input('>>:').strip()
    if len(msg) == 0:continue
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('recv:',data.decode())

client.close()
