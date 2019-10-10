#!/usr/bin/env python
# coding:utf-8
"""
Name : server端.py
Author  : anne
Time    : 2019-08-26 16:35
Desc:
"""
from socket import *
from multiprocessing import Process

server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)

def talk(conn,client_addr):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:break
            print(msg.decode('utf-8'))
            conn.send(msg.upper())
        except Exception:
            break


while True:
    conn,client_addr=server.accept()
    p=Process(target=talk,args=(conn,client_addr))
    p.start()


