#!/usr/bin/env python
# coding:utf-8
"""
Name : 服务端.py
Author  : anne
Time    : 2019-08-02 14:28
Desc:
"""

import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #声明socket类型同时生成socket链接对象
server.bind(('127.0.0.1',8000)) #绑定要监听的端口
server.listen(5)#监听
conn,addr=server.accept() #等待
print('我要开始等电话来')
print(conn,addr)
while True:
    msg = conn.recv(1024)   #收消息
    print('客户端发来的消息是：',msg)
    conn.send(msg.upper()) #发消息

conn.close()
server.close()