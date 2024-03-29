#!/usr/bin/env python
# coding:utf-8
"""
Name : client.py
Author  : anne
Time    : 2019-08-27 17:43
Desc:
"""
import socket
import os,sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class selectFtpClient:
    def __init__(self):
        self.args = sys.argv
        if len(self.args) > 1:
            self.port = (self.args[1],int(self.args[2]))
        else:
            self.port = ('127.0.0.1',8885)
        self.creat_socket()
        self.command_fanout()
    def creat_socket(self):
        try:
            self.sk = socket.socket()
            self.sk.connect(self.port)
            print('链接FTP服务器成功')
        except Exception as e:
            print('error:',e)


    def command_fanout(self):
        while True:
            cmd = input('>>>').strip()
            if cmd == 'exit()':
                break
            cmd,file = cmd.split()
            if hasattr(self,cmd):
                func = getattr(self,cmd)
                func(cmd,file)
            else:
                print('调用错误！')
    def put(self,cmd,file):
        if os.path.isfile(file):
            fileName = os.path.basename(file)
            fileSize = os.path.getsize(file)
            fileINfo = '%s|%s|%s'%(cmd,fileName,fileSize)
            self.sk.send(bytes(fileINfo,encoding='utf-8'))
            recvStatus = self.sk.recv(1024)
            print('recvStaus',recvStatus)
            hasSend = 0
            if str(recvStatus,encoding='utf-8') == 'OK':
                with open(file,'rb') as f:
                    while fileSize > hasSend:
                        contant = f.read(1024)
                        recv_size = len(contant)
                        self.sk.send(contant)
                        hasSend += recv_size
                        s = str(int(hasSend/fileSize*100))+'%'
                        print('正在上传文件:'+fileName+'已经上传:'+s)
                print('%文件上传完毕'%(fileName,))
            else:
                print('文件不存在')
    def get(self,cmd,file):
        pass

if __name__ == '__mian__':
    selectFtpClient()