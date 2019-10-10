#!/usr/bin/env python
# coding:utf-8
"""
Name : client_ftp.py
Author  : anne
Time    : 2019-08-05 12:19
Desc:
"""
import socket
import os
import hashlib

client = socket.socket()
client.connect(('127.0.0.1',9999))
while True:
    cmd = input('>>:').strip()
    if len(cmd) == 0:continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print('server response:',server_response)
        client.send(b'ready to recv file')
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + '.new','wb')
        m = hashlib.md5()
        #最后一次收数据的时候可能出现粘包现象,所以最后一次只收剩下的文件，
        # 不收1024大小的，防止把md5值也收到文件里
        while received_size < file_total_size:
            if file_total_size - received_size > 1024: #要收不止一次
                size = 1024
                print('last receive',size)
            else:#最后一次了，剩下多少收多少
                size = file_total_size - received_size
            data = client.recv(1024)
            received_size += len(data)
            m.update(data)
            f.write(data)
            # print(file_total_size,received_size)
        else:
            new_file_md5 = m.hexdigest()
            print('file recv done',received_size,file_total_size)
            f.close()
        server_file_md5 = client.recv(1024)
        print('server file md5:',server_file_md5)
        print('client file md5',new_file_md5)

client.close()

