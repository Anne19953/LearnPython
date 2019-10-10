#!/usr/bin/env python
# coding:utf-8
"""
Name : rpc_server.py
Author  : anne
Time    : 2019-09-02 21:01
Desc:
"""
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='rpc_queue')  #绑定取消息的队列


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#处理请求的方法
def on_request(ch, method, props, body):
    n = int(body)  #消息主题为str格式需要转成int

    print(" [.] fib(%s)" % n)
    response = fib(n)  #调用fib()，生成返回结果

    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,#返回指定队列
                     properties=pika.BasicProperties(correlation_id=
                        props.correlation_id),#将请求附带的correlation_id返回
                     body=str(response)) #将结果转成str返回
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume('rpc_queue',on_request)  #从rpc_queue取消息，并调用on_request方法处理

print(" [x] Awaiting RPC requests")
channel.start_consuming()