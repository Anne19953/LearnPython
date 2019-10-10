#!/usr/bin/env python
# coding:utf-8
"""
Name : client.py
Author  : anne
Time    : 2019-08-28 14:21
Desc:自定制报文头部
"""
import socket, time, struct,json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
res = client.connect(('127.0.0.1', 8080))

while True:
    msg = input('>>: ').strip()
    if len(msg) == 0: continue
    if msg == 'quit': break

    client.send(msg.encode('utf-8'))

    head = client.recv(4)
    head_json_len = struct.unpack('i', head)[0]
    head_json = json.loads(client.recv(head_json_len).decode('utf-8'))
    data_len = head_json['data_size']
    receive_size = 0
    receive_data = b''
    while receive_size < data_len:
        receive_data = client.recv(1024)
        receive_size += len(receive_data)

    print(receive_data.decode('utf-8'))
    # print(data.decode('gbk'))  # windows默认gbk编码
