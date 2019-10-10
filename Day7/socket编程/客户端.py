#!/usr/bin/env python
# coding:utf-8
"""
Name : 客户端.py
Author  : anne
Time    : 2019-08-02 14:28
Desc:
"""
import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    #声明socket类型同时生成socket链接对象

client.connect(('127.0.0.1',8000)) #链接对应IP和端口


while True:
    msg = input('>>').strip()
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print('收到服务端发来的消息：',data)