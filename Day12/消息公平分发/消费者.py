#!/usr/bin/env python
# coding:utf-8
"""
Name : 消费者.py
Author  : anne
Time    : 2019-09-02 17:04
Desc:
"""
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='127.0.0.1'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume('task_queue',callback,False)

channel.start_consuming()