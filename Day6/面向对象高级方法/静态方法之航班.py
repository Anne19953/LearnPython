#!/usr/bin/env python
# coding:utf-8
"""
Name : 静态方法之航班.py
Author  : anne
Time    : 2019-07-31 15:43
Desc:
"""

class Flight(object):
    def __init__(self, flignt_name):
        self.name = flignt_name

    def checking_status(self):
        print('checking flight %s status' % self.name)
        return 1

    @property
    def flight_stastus(self):
        status = self.checking_status()
        if status == 0:
            print('flight got cancled...')
        elif status == 1:
            print('flight is arrived...')
        elif status == 2:
            print('flight has departured already...')
        else:
            print('connot confirm the flight status...,please check later')

    @flight_stastus.setter  #修改
    def flight_status(self,status):
        status_dic = {
            0:'canceled',
            1:'arriverd',
            2:'depatured'
        }
        print('\033[31;1mFlight %s has changed the flight status to %s \033[0m'%(self.name,status_dic.get(status)))

    @flight_status.deleter #删除
    def flight_status(self):
        print('status got removed...')


f = Flight('CA980')
f.flight_stastus
f.flight_status = 2  #触发@flight_status.setter
del f.flight_status  #触发@flight_status.deleter


