#!/usr/bin/env python
# coding:utf-8
"""
Name : send.py
Author  : anne
Time    : 2019-09-02 14:00
Desc:
"""
import pika
connection = pika.BlockingConnection(pika.ConnectionParameters(
               '127.0.0.1'))
channel = connection.channel()
#channel.queue_daclare(queue='hello',durable=True)
#声明queue
#n RabbitMQ a message can never be sent directly to the queue,
# it always needs to go through an exchange.
# channel.basic_publish(exchange='',routing_key='hello',body='hello Word!',
#                       properties=pika.BasicProperties(delivery_mode=2,))#消息持久化

channel.basic_publish(exchange='',routing_key='hello',body='hello Word!')
#
print("[x] sent 'Hello World !'")
connection.close()