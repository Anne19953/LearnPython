#!/usr/bin/env python
# coding:utf-8
"""
Name : receive.py
Author  : anne
Time    : 2019-09-02 14:15
Desc:
"""

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    'localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
#channel.queue_declare(queue='hello',durable=True)#只是将队列持久化，队列里面的消息并没有


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


#channel.basic_qos(prefetch_count=1) #如果接收者在处理消息，发送者就暂时不发
#channel.basic_consume(callback, queue=‘celery’, no_ack=True) 这样的参数位置在当前版本的pika不适用
#如果no_ack为True会出现消息丢失的情况
channel.basic_consume('hello',callback,False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
