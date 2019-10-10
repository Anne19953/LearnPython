#!/usr/bin/env python
# coding:utf-8
"""
Name : 消息publisher.py
Author  : anne
Time    : 2019-09-02 17:11
Desc:
"""
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')#之前写的type会报错

result = channel.queue_declare(queue='anne2')  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue_name,callback,True)

channel.start_consuming()