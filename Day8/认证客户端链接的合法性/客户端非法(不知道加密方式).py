#!/usr/bin/env python
# coding:utf-8
"""
Name : 客户端非法(不知道加密方式).py
Author  : anne
Time    : 2019-08-06 15:08
Desc:
"""
from socket import *


def client_handler(ip_port, bufsize=1024):
    tcp_socket_client = socket(AF_INET, SOCK_STREAM)
    tcp_socket_client.connect(ip_port)

    while True:
        data = input('>>: ').strip()
        if not data: continue
        if data == 'quit': break

        tcp_socket_client.sendall(data.encode('utf-8'))
        response = tcp_socket_client.recv(bufsize)
        print(response.decode('utf-8'))
    tcp_socket_client.close()


if __name__ == '__main__':
    ip_port = ('127.0.0.1', 9998)
    bufsize = 1024
    client_handler(ip_port, bufsize)
