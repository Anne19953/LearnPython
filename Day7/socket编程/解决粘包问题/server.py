#!/usr/bin/env python
# coding:utf-8
"""
Name : server.py
Author  : anne
Time    : 2019-08-28 14:21
Desc:自定制报文头部
"""
import socket, struct, json
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 就是它，在bind前加

server.bind(('127.0.0.1', 8080))

server.listen(5)

while True:
    conn, addr = server.accept()
    while True:
        cmd = conn.recv(1024)
        if not cmd: break
        print('cmd: %s' % cmd)

        res = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        err = res.stderr.read()
        print(err)
        if err:
            back_msg = err
        else:
            back_msg = res.stdout.read()

        headers = {'data_size':len(back_msg)} #定义报文头部
        head_json = json.dumps(headers)
        head_json_bytes = bytes(head_json,encoding='utf-8')
        conn.send(struct.pack('i', len(head_json_bytes)))  # 先发报头的长度
        conn.send(head_json_bytes)  # 再发报头
        conn.sendall(back_msg)  # 再发真实的内容

    conn.close()
