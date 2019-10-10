#!/usr/bin/env python
# coding:utf-8
"""
Name : server.py
Author  : anne
Time    : 2019-08-27 17:28
Desc:
"""
import os
import time
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
import socket
import selectors

class selectTtpServer:
    def __init__(self):
        self.dic = {}
        self.hasReceived = 0
        self.sel = selectors.DefaultSelector()
        self.create_socket()
        self.handle()
    #注册socket
    def create_socket(self):
        server = socket.socket()
        server.bind(('127.0.0.1',8885))
        server.listen(5)
        server.setblocking(False)  #设置为非阻塞
        self.sel.register(server,selectors.EVENT_READ,self.accept)
        print('服务端已开启，等待用户链接。。。')
    #监听
    def handle(self):
        while True:
            events = self.sel.select()  # 监听
            for key, mask in events:
                callback = key.data  # 第一次是accept函数的地址，如果监听到是conn变化就是read函数的地址
                callback(key.fileobj, mask)  # 执行accept(),key.fileobj 就是socket，
                # 执行read(),key.fileobj 就是conn

    def accept(self,sock,mask):
        conn, addr = sock.accept()
        print('accepted', conn, 'from', addr)
        conn.setblocking(False)
        self.sel.register(conn, selectors.EVENT_READ, self.read)  # 将conn与read函数进行绑定
        self.dic[conn] = {}
    def read(self,conn,mask):
        try:
            if not self.dic[conn]:
                data = conn.recv(1024)
                cmd,filename,filesize = str(data,encoding='utf-8').split('|')
                self.dic = {conn:{'cmd':cmd,'filename':filename,'filesize':int(filesize)}}
            if cmd == 'put':
                conn.send(bytes('OK',encoding='utf-8'))
            if self.dic[conn]['cmd'] == 'get':
                file = os.path.join(BASE_DIR,'download',filename)
                if os.path.exists(file):
                    filesize = os.path.getsize(file)
                    send_info = '%s|%s'%('YES',filesize)
                    conn.send(bytes(send_info,encoding='utf-8'))
                else:
                    send_info = '%s|%s'%('NO',0)
                    conn.send(bytes(send_info,encoding='utf-8'))
            else:
                if self.dic[conn].get('cmd',None):
                    cmd = self.dic[conn].get('cmd')
                    if hasattr(self,cmd):
                        func = getattr(self,cmd)
                        func(conn)
                    else:
                        print('error cmd!')
        except Exception as e:
            print('error',e)
            self.sel.unregister(conn)
            conn.close()




    def put(self,conn):
        fileName = self.dic[conn]['filename']
        fileSize = self.dic[conn]['filesize']
        path = os.path.join(BASE_DIR,'upload',fileName)
        recv_data = conn.recv(1024)
        self.hasReceived += len(recv_data)

        with open(path,'ab') as f:
            f.write(recv_data)
        if fileSize == self.hasReceived:
            if conn in self.dic.keys():
                self.dic[conn] = {}
            print('%s 上传完毕！'%fileName)
    def get(self,conn):
        pass



if __name__ == '__main__':
    selectTtpServer()

