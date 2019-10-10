#!/usr/bin/env python
# coding:utf-8
"""
Name : server.py
Author  : anne
Time    : 2019-08-06 16:05
Info:server端的任务处理在这里
"""

import socketserver
import json
import configparser
from conf import settings
import os

STATUS_CODE = {
    250: "Invalied cmd format,e.g : {'action':'get','filename':'test.py','size':344}",
    251: 'Invalid cmd',
    252: 'Invalid auth data',
    253: 'Wrong username or password',
    254: 'Passed authentication',
    255: 'Filename doesn\'t provided',
    256: 'File doesn\'t exist on server',
    257: 'ready to send file',
    258: 'md5 verification',

    800: 'the file exist,but not enough,is continue?',
    801: 'the file exist !',
    802: 'ready to receive datas',

    900: 'md5 valdate success'
}


class ServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while 1:
            # cnn = self.request
            # 接受来自client的请求验证消息(就这一个小问题找了两天，哭廖～～)
            data = self.request.recv(1024).strip()
            # 将json字符串解析为python字典格式
            data = json.loads(data.decode('utf-8'))
            """
            格式如下：
             { 'action':'auth',
               'usename':'yuan,
               'pwd':123
            }
            
            """
            if data.get('action'):
                if hasattr(self, data.get('action')):
                    func = getattr(self, data.get('action'))
                    func(**data)
                # 写的命令不存在
                else:
                    print('invalid cmd')
            # action后面没写命令
            else:
                print('Invalid cmd')

    def send_response(self, state_code):
        """向客户端返回数据"""
        response = {'status_code': state_code}
        self.request.sendall(json.dumps(response).encode('utf-8'))
    ############################################登陆验证
    def auth(self, **data):
        username = data["username"]
        passeord = data["password"]
        # 验证
        user = self.authenticate(username, passeord)
        if user:
            self.send_response(254)
        else:
            self.send_response(253)

    def authenticate(self, user, pwd):
        cfg = configparser.ConfigParser()
        cfg.read(settings.ACCOUNT_PATH)
        if user in cfg.sections():
            if cfg[user]['Password'] == pwd:
                # 登陆成功后，获得用户信息
                self.user = user
                self.mainPath = os.path.join(settings.BASE_DIR,'home',self.user)
                print('passed authentication!')
                return user

    ############################################上传文件
    def put(self, **data):
        print('data',data)
        file_name = data.get('file_name')
        file_size = data.get('file_size')
        target_path = data.get('target_path')
        abs_path = os.path.join(self.mainPath,target_path,file_name)


        ####################
        has_received = 0
        if os.path.exists(abs_path):
            has_file_size = os.stat(abs_path).st_size
            if has_file_size < file_size:
            #断点续传
                self.request.sendall('800'.encode('utf-8'))
                choice = self.request.recv(1024).decode('utf-8')
                if choice == 'Y':
                    self.request.sendall(str(has_file_size).encode('utf-8'))
                    has_file_size += has_file_size
                    f = open(abs_path,'ab')
                else:
                    f = open(abs_path,'wb')
            else:
                #文件完整存在
                self.request.sendall('801'.encode('utf-8'))
                print('the file exits!')
                #这种情况就不往下走了，直接返回
                return
        else:
            self.request.sendall('802'.encode('utf-8'))
            f = open(abs_path, 'wb')
        while has_received < file_size:
            #接受的大小小于文件大小时，一直接受
            try:
                data = self.request.recv(1024)
            except Exception as e:
                break
            f.write(data)
            has_received += len(data)

        f.close()

    def ls(self,**data):

        file_list = os.listdir(self.mainPath)
        file_str = '\n'.join(file_list)
        if not len(file_list):
        #如果该目录下没有内容
            file_str = '<empty dir>'
        self.request.sendall(file_str.encode('utf-8'))

    def cd(self,**data):
        dirname = data.get('dirname')
        if dirname == '..':
            self.mainPath = os.path.dirname(self.mainPath)
        else:
            self.mainPath = os.path.join(self.mainPath,dirname)

        self.request.sendall(self.mainPath.encode('utf-8'))

    def makdir(self,**data):
        dirname = data.get('dirname')
        path = os.path.join(self.mainPath,dirname)
        #判断该文件夹是否存在
        if not os.path.exists(path):
            if '/' in dirname:
                os.makedirs(path)
            else:
                os.mkdir(path)
            self.request.sendall('dirname success'.encode('utf-8'))
        else:
            self.request.sendall('dirname exist'.encode('utf-8'))




