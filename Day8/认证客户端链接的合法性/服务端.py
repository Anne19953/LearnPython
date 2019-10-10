#!/usr/bin/env python
# coding:utf-8
"""
Name : 服务端.py
Author  : anne
Time    : 2019-08-06 15:07
Desc:
"""
from socket import *
import hmac, os

secret_key = b'anne is best'


def conn_auth(conn):
    '''
    认证客户端链接
    :param conn:
    :return:
    '''
    print('开始验证新链接的合法性')
    msg = os.urandom(32) # 随机产生一个32位的密钥
    print(msg)
    conn.sendall(msg)  #将这32位密码发送给client端
    h = hmac.new(secret_key, msg)  # hmac类似于md5,这里是加盐的方式
    digest = h.digest()   #生成密文
    respone = conn.recv(len(digest))    #接收来自client的验证密文
    return hmac.compare_digest(respone, digest)  #比对是否一致


def data_handler(conn, bufsize=1024):
    if not conn_auth(conn):
        print('该链接不合法,关闭')
        conn.close()
        return
    print('链接合法,开始通信')
    while True:
        data = conn.recv(bufsize)
        if not data: break
        conn.sendall(data.upper())


def server_handler(ip_port, bufsize, backlog=5):
    '''
    只处理链接
    :param ip_port:
    :return:
    '''
    tcp_socket_server = socket(AF_INET, SOCK_STREAM)
    tcp_socket_server.bind(ip_port)
    tcp_socket_server.listen(backlog)
    while True:
        conn, addr = tcp_socket_server.accept()
        print('新连接[%s:%s]' % (addr[0], addr[1]))
        data_handler(conn, bufsize)


if __name__ == '__main__':
    ip_port = ('127.0.0.1', 9998)
    bufsize = 1024
    server_handler(ip_port, bufsize)
