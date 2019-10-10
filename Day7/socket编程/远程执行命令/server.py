#!/usr/bin/env python
# coding:utf-8
"""
Name : server.py
Author  : anne
Time    : 2019-08-28 09:59
Desc:
"""
from socket import *
import subprocess
tcp_socket_server=socket(AF_INET,SOCK_STREAM)
tcp_socket_server.bind(('127.0.0.1',8080))
tcp_socket_server.listen(5)

while True:
    conn,addr=tcp_socket_server.accept()
    print('客户端',addr)

    while True:
        cmd=conn.recv(1024)     #接收来自client发送的命令
        if len(cmd) == 0:break
        #执行命令
        act_res=subprocess.Popen(cmd.decode('utf-8'),shell=True,
                         stdout=subprocess.PIPE,
                         stdin=subprocess.PIPE,
                         stderr=subprocess.PIPE)

        stderr=act_res.stderr.read()  #标准错误
        stdout=act_res.stdout.read()  #执行结果的标准输出
        conn.send(stderr)  #向client端返回执行结果
        conn.send(stdout)  #向client端返回错误信息
