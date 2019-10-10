#!/usr/bin/env python
# coding:utf-8
"""
Name : 客户端合法.py
Author  : anne
Time    : 2019-08-06 15:07
Desc:
"""
from socket import *
import hmac, os

secret_key = b'anne is best'


def conn_auth(conn):
    '''
    验证客户端到服务器的链接
    :param conn:
    :return:
    '''
    msg = conn.recv(32)  #接收来自server的原始密钥
    h = hmac.new(secret_key, msg)
    digest = h.digest()  #生成最终秘文
    conn.sendall(digest) #发送秘文给客户端


def client_handler(ip_port, bufsize=1024):
    tcp_socket_client = socket(AF_INET, SOCK_STREAM)
    tcp_socket_client.connect(ip_port)

    conn_auth(tcp_socket_client)

    while True:
        data = input('>>: ').strip()
        if not data: continue
        if data == 'quit': break

        tcp_socket_client.sendall(data.encode('utf-8'))
        respone = tcp_socket_client.recv(bufsize)
        print(respone.decode('utf-8'))
    tcp_socket_client.close()


if __name__ == '__main__':
    ip_port = ('127.0.0.1', 9998)
    bufsize = 1024
    client_handler(ip_port, bufsize)
