#!/usr/bin/env python
# coding:utf-8
"""
Name : client.py
Author  : anne
Time    : 2019-08-28 09:59
Desc:
"""
import socket


tcp_socket_client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
res=tcp_socket_client.connect(('127.0.0.1',8080))

while True:
    msg=input('>>: ').strip()
    if len(msg) == 0:continue
    if msg == 'quit':break

    tcp_socket_client.send(msg.encode('utf-8'))  #向server端发送执行命令
    act_res=tcp_socket_client.recv(1024)  #接收执行完命令返回的结果

    print(act_res.decode('utf-8'),end='')