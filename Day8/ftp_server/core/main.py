#!/usr/bin/env python
# coding:utf-8
"""
Name : main.py
Author  : anne
Time    : 2019-08-06 15:29
Info:对启动命令进行解析，比如输入'python ftp_server start ',
获取start命令，并调用start函数，
同理如果输入'python ftp_server help'，
获取help命令，并调用help方法
"""

# 解析命令行命令
import optparse
import socketserver
# 可以这样导入是因为在ftp_server已经添加了ftp_server路径
from conf import settings
from core import server


class ArgvHandler():
    def __init__(self):
        self.op = optparse.OptionParser()
        # self.op.add_option('-s','--server',dest='server')
        # self.op.add_option('-p','--port',dest='port')
        # 参数解析 返回绑定了的参数(server,port对应的参数)到options，返回未绑定的参数到args
        # options的属性为对象，要获取ip用options.server
        options, args = self.op.parse_args()
        self.verify_args(options, args)

    # 对命令进行分发，将启动命令传入
    def verify_args(self, options, args):
        # 因为未进行绑定，返回的参数在args中
        cmd = args[0]
        # 反射
        # 不同命令去调用不同方法
        if hasattr(self, cmd):
            func = getattr(self, cmd)
            func()

    # 启动socketsever
    def start(self):
        print('the server is working...')
        s = socketserver.ThreadingTCPServer((settings.IP, settings.PORT), server.ServerHandler)
        # 处理多个请求
        s.serve_forever()

    def help(self):
        pass
