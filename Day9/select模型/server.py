#!/usr/bin/env python
# coding:utf-8
"""
Name : server.py
Author  : anne
Time    : 2019-08-27 11:20
Desc:多路复用实现并发聊天
"""
# import socket
# import select
# sk = socket.socket()
# sk.bind(('127.0.0.1',9904))
# sk.listen(5)
# inp = [sk,]  #socket对象
# while True:
#
#     r,w,e = select.select(inp,[],[])  #[sk,conn]链接变多时，sk变化
#     for i in r:#[sk]
#         conn,add = i.accept()
#         print(conn)
#         print('hello')
#         inp.append(conn)  #当client发送数据时，conn变化
#         data = conn.recv(1024).decode('utf-8')
#         print(data)
#
#     print('>>>>>>>>>>>>>>>>>')



#***********************server.py
import socket
import select
sk=socket.socket()
sk.bind(("127.0.0.1",8801))
sk.listen(5)
inputs=[sk,]
while True:
    r,w,e=select.select(inputs,[],[],5)
    print(len(r))

    for obj in r: #需要判断r里面的是sk还是conn ,sk表示新的socket链接进来了
                #conn表示客户端在发消息
        if obj==sk:
            conn,add=obj.accept()
            print(conn)
            inputs.append(conn)
        else:
            data_byte=obj.recv(1024)
            print(str(data_byte,'utf8'))
            inp=input('回答%s号客户>>>'%inputs.index(obj))
            obj.sendall(bytes(inp,'utf8'))

    print('>>',r)

