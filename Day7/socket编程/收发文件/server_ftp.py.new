#!/usr/bin/env python
# coding:utf-8
"""
Name : server_ftp.py
Author  : anne
Time    : 2019-08-05 12:18
Desc:
"""

import socket
import os,hashlib
server = socket.socket()
server.bind(('127.0.0.1',9999))
server.listen()
while True:
    conn,addr = server.accept()
    print('new conn:',addr)
    while True:
        print('等待新指令')
        data = conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        cmd,filename = data.decode().split()
        print(filename)
        #判断文件是否存在
        if os.path.isfile(filename):
            m = hashlib.md5()
            f = open(filename,'rb')
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode()) #send file size
            conn.recv(1024) #wait for ack
            for line in f:
                m.update(line)
                conn.send(line)
            print('file md5',m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
        print('send down')
server.close()


