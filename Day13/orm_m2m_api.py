#!/usr/bin/env python
# coding:utf-8
"""
Name : orm_m2m_api.py
Author  : anne
Time    : 2019-09-05 11:59
Desc:
"""
import orm_m2m
from sqlalchemy.orm import sessionmaker
Session_class = sessionmaker(bind=orm_m2m.engine) #创建与数据库的会话session class,注意返回给session的是个class不是实例
Session = Session_class()    #生成session实例  #类似与cursor

b1 = orm_m2m.Book(name="跟Alex学Python",pub_date='2018-09-09')
b2 = orm_m2m.Book(name="跟Alex学把妹",pub_date='2018-07-09')
b3 = orm_m2m.Book(name="跟Alex学装逼",pub_date='2018-06-09',)

a1 = orm_m2m.Author(name="Alex")
a2 = orm_m2m.Author(name="Jack")
a3 = orm_m2m.Author(name="Rain")

b1.authors = [a1, a2]
b2.authors = [a1, a2, a3]

Session.add_all([b1, b2, b3, a1, a2, a3])

author_obj = Session.query(orm_m2m.Author).filter(orm_m2m.Author.name=='Alex').first()
print(author_obj.books)

book_obj = Session.query(orm_m2m.Book).filter(orm_m2m.Book.id==2).first()
print(book_obj.authors)

Session.commit()