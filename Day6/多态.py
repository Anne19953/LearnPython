#!/usr/bin/env python
# coding:utf-8
"""
Name : 多态.py
Author  : anne
Time    : 2019-07-30 21:08
Desc:
"""
class Animal(object):
    def __init__(self,name):
        self.name = name
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')
class Cat(Animal):
    def talk(self):
        print('%s:喵喵喵!' %self.name)

class Dog(Animal):
    def talk(self):
        print('%s: 汪汪汪！' %self.name)

def func(obj):
    obj.talk()

c1 = Cat('小晴')
d1 = Dog('小明')

func(c1)
func(d1)

