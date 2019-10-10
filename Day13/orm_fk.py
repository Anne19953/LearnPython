#!/usr/bin/env python
# coding:utf-8
"""
Name : orm_fk.py
Author  : anne
Time    : 2019-09-04 18:20
Desc:
"""
import sqlalchemy
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String ,DATE ,Enum ,ForeignKey

engine = create_engine("mysql+pymysql://root@localhost/anne",
                       encoding='utf-8')  #echo=True有echo会打印执行过程

Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = 'student'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)

    # 打印结果可以区分出来id和name
    def __repr__(self):
        return '<%s name: %s>' % (self.id, self.name)

class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))
    student = relationship('Student',backref='my_study_record') #在student表里查study_record使用my_study_record字段
                                                              #在study_record里面查student使用student字段

    # 打印结果可以区分出来id和name
    def __repr__(self):
        return '<%s day:%s status:%s>' % (self.student.name, self.day,self.status)

Base.metadata.create_all(engine)  # 创建表结
Session_class = sessionmaker(bind=engine) #创建与数据库的会话session class,注意返回给session的是个class不是实例
Session = Session_class()    #生成session实例  #类似与cursor

# s1 = Student(name='Alex',register_date='2019-4-26')
# s2 = Student(name='Anne',register_date='2019-5-25')
# s3 = Student(name='Songfengju',register_date='2019-3-26')
# s4 = Student(name='eee',register_date='2019-2-26')
#
# study_obj1 = StudyRecord(day=1,status='YES',stu_id=1)
# study_obj2 = StudyRecord(day=2,status='YES',stu_id=1)
# study_obj3 = StudyRecord(day=3,status='YES',stu_id=1)
# study_obj4 = StudyRecord(day=1,status='YES',stu_id=2)
#
# Session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])

stu_obj = Session.query(Student).filter(Student.name=='Alex').first()
print(stu_obj.my_study_record)
Session.commit()

