#!/usr/bin/env python
# coding:utf-8
"""
Name : 进程queue.py
Author  : anne
Time    : 2019-08-23 17:46
Desc:
"""
from multiprocessing import Process, Queue


# def f(q):
#     q.put([42, None, 'hello'])
#
#
# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())  # prints "[42, None, 'hello']"
#     p.join()


q=Queue(3)


#put ,get ,put_nowait,get_nowait,full,empty
q.put(3)
q.put(3)
q.put(3)
print(q.full()) #满了

print(q.get())
print(q.get())
print(q.get())
print(q.empty()) #空了