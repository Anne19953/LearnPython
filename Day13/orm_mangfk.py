#!/usr/bin/env python
# coding:utf-8
"""
Name : orm_mangfk.py
Author  : anne
Time    : 2019-09-05 10:56
Desc:
"""
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


#数据库需要支持中文 mysql+pymysql://root@localhost/anne?charset=utf8
engine = create_engine("mysql+pymysql://root@localhost/anne",
                       encoding='utf-8')  #echo=True有echo会打印执行过程

Base = declarative_base()  # 生成orm基类


class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    billing_address_id = Column(Integer, ForeignKey("address.id"))
    shipping_address_id = Column(Integer, ForeignKey("address.id"))

    #此处不加上外键的话无法区分出来对应的是那个
    billing_address = relationship("Address", foreign_keys=[billing_address_id])
    shipping_address = relationship("Address", foreign_keys=[shipping_address_id])


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street = Column(String(32))
    city = Column(String(32))
    state = Column(String(32))

    def __repr__(self):
        return self.street


Base.metadata.create_all(engine)  # 创建表结构