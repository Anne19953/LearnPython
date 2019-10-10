#!/usr/bin/env python
# coding:utf-8
"""
Name : orm_api.py
Author  : anne
Time    : 2019-09-05 10:50
Desc:
"""
import orm_mangfk
from sqlalchemy.orm import sessionmaker

Session_class = sessionmaker(bind=orm_mangfk.engine) #创建与数据库的会话session class,注意返回给session的是个class不是实例
Session = Session_class()    #生成session实例  #类似与cursor

addr1 = orm_mangfk.Address(street='Tiantongyuan',city='ChangPing',state='BJ')
addr2 = orm_mangfk.Address(street='Wudaokou',city='Haidian',state='BJ')
addr3 = orm_mangfk.Address(street='Yanjiao',city='LangFang',state='HB')

Session.add_all([addr1,addr2,addr3])
c1 = orm_mangfk.Customer(name='Alex',billing_address=addr1,shipping_address=addr2)
c2 = orm_mangfk.Customer(name='Jack',billing_address=addr3,shipping_address=addr2)
Session.add_all([c1,c2])
Session.commit()

obj = Session.query(orm_mangfk.Customer).filter(orm_mangfk.Customer.name=='Alex').first()
print(obj.name,obj.billing_address,obj.shipping_address)