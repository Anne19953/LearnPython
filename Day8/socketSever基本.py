#!/usr/bin/env python
# coding:utf-8
"""
Name : socketSever基本.py
Author  : anne
Time    : 2019-08-05 14:31
Desc:
"""
import socketserver
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote'.format(self.client_address[0]))
                print(self.data.decode())
                self.request.send(self.data.upper())
            except ConnectionResetError as e :
                print('err',e)
                break
if __name__ == '__main__':
    HOST,PORT = '127.0.0.1',9999
    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)
    server.serve_forever()
    server.server_close()
