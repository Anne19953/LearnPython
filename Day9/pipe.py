#!/usr/bin/env python
# coding:utf-8
"""
Name : pipe.py
Author  : anne
Time    : 2019-08-25 10:41
Desc:
"""
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.send(['from child'])
    print(conn.recv())
    conn.close()



if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    print(parent_conn.recv())
    parent_conn.send('from child')

    p.join()
