#!/usr/bin/env python
# coding:utf-8
"""
Name : csplay.py
Author  : anne
Time    : 2019-07-29 20:45
Desc:
"""


class Role(object):
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        #构造函数
        #在实例化时做一些类的初始化的工作
        self.name = name  #实例变量(静态属性)，作用域是实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value  #变为私有属性
        self.money = money
    # def __del__(self):
        #析构函数
        # print('%s 彻底死了' %self.name)

    def shot(self):#（动态属性）

        print("shooting...")
#要访问私有属性，需要通过调用特定方法访问
    def got_shot(self):
        self.__life_value -= 50
        print("ah...,I got shot...")

    def get_status(self):
        print('name : %s ,weapon : %s,__life_value : %s' %(self.name,self.weapon,self.__life_value))
    def buy_gun(self, gun_name):
        print("%s just bought %s" % (self.name,gun_name))

r1 = Role('Alex','police','AK47') #实例化(初始化一个类，造一个对象)
# print(r1.__life_value)  #私有属性无法直接访问

r2 = Role('Jack','terrorist','B22') #生成一个角色

r1.buy_gun('AK47')
r1.got_shot()
r1.get_status()
r2.buy_gun('B22')

