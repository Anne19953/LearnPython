#!/usr/bin/env python
# coding:utf-8
"""
Name : 生产者.py
Author  : anne
Time    : 2019-09-02 16:58
Desc:在各个消费者端，配置perfetch=1,
意思就是告诉RabbitMQ在我这个消费者当前消息还没处理完的时候就不要再给我发新消息了。
"""
import pika
import sys
connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()
channel.queue_declare(queue='task_queue',durable=True)
message = 'Hello World!'
channel.basic_publish(exchange='',routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2,))
print('[x] sent %r' %message)
connection.close()

