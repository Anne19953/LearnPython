#!/usr/bin/env python
# coding:utf-8
"""
Name : creat_table.py
Author  : anne
Time    : 2019-09-04 14:35
Desc:
"""
import sqlalchemy
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String ,DATE ,Enum

engine = create_engine("mysql+pymysql://root@localhost/anne",
                       encoding='utf-8')  #echo=True有echo会打印执行过程

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

#打印结果可以区分出来id和name
    def __repr__(self):
        return '<%s name: %s>' %(self.id,self.name)


class Student(Base):
    __tablename__ = 'student'  # 表名
    stu_id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    age = Column(Integer)
    register_date = Column(DATE,nullable=False)
    sex = Column(Enum('M',"F"),nullable=False)

    # 打印结果可以区分出来id和name
    def __repr__(self):
        return '<%s name: %s>' % (self.stu_id, self.name)


Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class,注意返回给session的是个class不是实例
Session = Session_class()    #生成session实例  #类似与cursor
#
# user_obj1= User(name='anne',password='22334') #生成你要创建的对象
# user_obj2 = User(name='haha',password='1234')
# user_obj3 = User(name='lili',password='1222')
# user_obj4 = User(name='zhu',password='77742')


# Session.add(user_obj1)   #把要创建的数据对象添加到这个session里
# Session.add(user_obj2)
# Session.add(user_obj4)
# Session.commit()
#Session.commit() #现在才统一提交

#查询
# my_user = Session.query (User).filter_by(name='anne').first()
# print(my_user.id,my_user.name,my_user.password)

#多个查询
# data = Session.query(User).filter(User.id > 1).filter(User.id<4).all()
# print(data)

#修改
# data = Session.query(User).filter(User.id ==1).first()
# data.name = 'jiangfan'
# data.password = 'idontknow'
# Session.commit()

#回滚
# fake_user = User(name='Rain',password='123456')
# Session.add(fake_user)
# print(Session.query(User).filter(User.name.in_(['jack','rain'])).all())
# Session.rollback() #回滚
# print('after rollback-----------')
# print(Session.query(User).filter(User.name.in_(['jack','rain'])).all())
# Session.commit()

#统计和分组

# print(Session.query(User).filter(User.name.like('ji%')).count())
# print(Session.query(User).filter(User.name.in_(['songfengju','jiangfan'])).count())

#分组
# print(Session.query(func.count(User.name),User.name).group_by(User.name).all())

#连表
print(Session.query(User,Student).filter(User.id == Student.stu_id).all())
ret = Session.query(User).join(Student).all()
Session.commit()

