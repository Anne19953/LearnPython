#!/usr/bin/env python
# coding:utf-8
"""
Name : 继承.py
Author  : anne
Time    : 2019-07-30 17:03
Desc:
"""
#peple是父类，man 和 woman 是子类
#子类可以继承父类的方法，子类之间独有的方法不可以共享
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('%s is eating...'%self.name)
    def talk(self):
        print('%s is talking...' %self.name)
    def sleep(self):
        print('%s is sleeping...'%self.name)

class Relation(object):
    friends = []
    def make_friends(self,obj):
        print('%s is making friends with %s'%(self.name,obj.name))
        # self.friends.append(obj.name)

class Man(People,Relation):
    def __init__(self,name,age,money):
        #新式继承方法
        super(Man,self).__init__(name,age)
        #People.__init__(self,name,age)
        self.money = money
        print('%s 一出生就有 %s 元'%(self.name,self.money))

    def sleep(self):
        People.sleep(self)     #继承父类方法
        print('man is sleeping....')
    pass



class Woman(People,Relation):
    def get_birthday(self):
        print('%s is getting birth...'%self.name)

m1 = Man('anne',13,200)
w1 = Woman('yanfei',44)
m1.make_friends(w1)

w1.name = 'lehong'
print(m1.make_friends(w1))