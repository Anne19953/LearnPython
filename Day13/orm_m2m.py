#!/usr/bin/env python
# coding:utf-8
"""
Name : orm_m2m.py
Author  : anne
Time    : 2019-09-05 11:57
Desc:
"""
#一本书可以有多个作者，一个作者又可以出版多本书


from sqlalchemy import Table, Column, Integer,String,DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root@localhost/anne",
                       encoding='utf-8')  #echo=True有echo会打印执行过程

Base = declarative_base()

#因为该表不需要向用户展示，所以没必要建成类的形式
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id',Integer,ForeignKey('books.id')),
                        Column('author_id',Integer,ForeignKey('authors.id')),
                        )

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer,primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    authors = relationship('Author',secondary=book_m2m_author,backref='books')

    def __repr__(self):
        return self.name

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name



Base.metadata.create_all(engine)  # 创建表结构