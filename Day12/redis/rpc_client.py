#!/usr/bin/env python
# coding:utf-8
"""
Name : rpc_client.py
Author  : anne
Time    : 2019-09-02 21:00
Desc:
"""
import pika
import uuid


class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))

        self.channel = self.connection.channel()

        result = self.channel.queue_declare('anne')  #绑定返回队列，随机生成
        self.callback_queue = result.method.queue

        self.channel.basic_consume(self.callback_queue,self.on_response,True,
                                   ) #从绑定的返回队列取结果

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:  #检测是否与发送的corr_id一致
            self.response = body  #取出返回结果传给response

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())    #生成唯一的corr_id
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',  #发送的队列
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,  #返回的队列
                                       correlation_id=self.corr_id, #发送corr_id
                                   ),
                                   body=str(n))#消息主体
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(30)")
response = fibonacci_rpc.call(30)  #调用Call()方法
print(" [.] Got %r" % response)  #打印返回结果