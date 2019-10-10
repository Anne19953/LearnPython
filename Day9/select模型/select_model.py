#!/usr/bin/env python
# coding:utf-8
"""
Name : select_model.py
Author  : anne
Time    : 2019-08-27 14:02
Desc:selectors模块，实现多并发，多个client端向server发消息
"""
import selectors
import socket
sel = selectors.DefaultSelector()  #不同平台提供的多路复用方式不同，select,poll,epoll,自行选择合适的方法

def accept(sock,mask):
    conn,addr = sock.accept()
    print('accepted',conn,'from',addr)
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)  #将conn与read函数进行绑定

def read(conn,mask):
    data = conn.recv(1000)
    if data:
        print('echoing',repr(data),'to',conn)
        conn.send(data)
    else:
        print('closing',conn)
        sel.unregister(conn)   #如果客户端链接断了，就解除绑定，删除此conn
        conn.close()

sock = socket.socket()
sock.bind(('127.0.0.1',8801))
sock.listen(1000)
sock.setblocking(False)  #设置为非阻塞
sel.register(sock,selectors.EVENT_READ,accept)  #注册，将sock与accept绑定
print('server........')
while True:
    events = sel.select()   #监听
    for key,mask in events:
        callback = key.data #第一次是accept函数的地址，如果监听到是conn变化就是read函数的地址
        callback(key.fileobj,mask)  #执行accept(),key.fileobj 就是socket，
                                    # 执行read(),key.fileobj 就是conn
