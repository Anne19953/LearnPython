#!/usr/bin/env python
# coding:utf-8
"""
Name : 智能机器人_服务端.py
Author  : anne
Time    : 2019-08-02 17:19
Desc:
"""
import socket
server = socket.socket()
server.bind(('127.0.0.1',8888))
server.listen(5)

while True:
    conn,addr = server.accept()
    conn.sendall('欢迎致电10086，请输入1xxx,0转人工服务'.encode('utf-8'))
    Flag = True
    while Flag:
        data = conn.recv(1024).decode()
        if data == 'exit':
            Flag = False
        elif data == '0':
            conn.sendall('通过可能会被录音。。'.encode('utf-8'))
        else:
            conn.sendall('请重新输入'.encode('utf-8'))
    conn.close()
server.close()
