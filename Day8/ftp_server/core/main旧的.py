#!/usr/bin/env python
# coding:utf-8
"""
Name : socketSever基本.py
Author  : anne
Time    : 2019-08-05 14:31
Desc:
"""
import socketserver,json,os
class MyTCPHandler(socketserver.BaseRequestHandler):
    def put(self,*args):
        """接受客户端文件"""
        cmd_dic = args[0]
        filename = cmd_dic['filename']
        filesize = cmd_dic['size']
        if os.path.isfile(filename):
            f = open(filename + '.new','wb')
        else:
            f = open(filename,'wb')
        self.request.send(b'200 ok')
        received_size = 0
        while received_size < filesize:
            data = self.request.recv(1024)
            f.write(data)
            received_size += len(data)
        else:
            print('file [%s] has uploaded...'%filename)




    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote'.format(self.client_address[0]))
                print(self.data.decode())
                cmd_dic = json.loads(self.data.decode())
                action = cmd_dic['action']
                if hasattr(self.action):
                    func = getattr(self.action)
                    func(cmd_dic)
                self.request.send(self.data.upper())
            except ConnectionResetError as e :
                print('err',e)
                break
if __name__ == '__main__':
    HOST,PORT = '127.0.0.1',9999
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
