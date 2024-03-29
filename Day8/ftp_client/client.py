#!/usr/bin/env python
# coding:utf-8
"""
Name : client.py
Author  : anne
Time    : 2019-08-05 15:59
Desc:
"""
import socket
import os,json



class FtpClient(object):
    def __init__(self):
        self.client = socket.socket()
    def help(self):
        msg = """
            ls
            pwd
            cd .. 
            get filename
            put filename
        
        """
    def connect(self,ip,port):
        self.client.connect((ip,port))
    def interactive(self):
        #self.authenticate()   登陆认证
        while True:
            cmd = input('>>').strip()
            if len(cmd) == 0 :continue
            cmd_str = cmd.split()[0]
            if hasattr(self,'cmd_%s' %cmd_str):
                func = getattr(self,'cmd_%s' % cmd_str)
                func(cmd)
            else:
                self.help()
    def cmd_put(self,*args):
        cmd_split = args[0].split()
        if len(cmd_split) > 1:
            filename = cmd_split[1]
            if os.path.isfile(filename):
                filesize = os.stat(filename).st_size
                msg_str = '%s|%s' %(filename,filesize)
                msg_dic = {
                    'action':'put',
                    'filename':filename,
                    'size':filesize,
                    'overridden':True
                }
                self.client().send(json.dumps(msg_dic).encode('utf-8'))
                #防止粘包，等服务器确认
                server_response= self.client.recv(1024)
                f = open(filename,'rb')
                for line in f :
                    self.client.send(line)
                else:
                    print('file upload success...')
                    f.close()
            else:
                print(filename,'is not exist')

    def cmd_get(self):
        pass

ftp = FtpClient()
ftp.connect('127.0.0.1',9999)
ftp.interactive()

