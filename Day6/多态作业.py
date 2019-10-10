#!/usr/bin/env python
# coding:utf-8
"""
Name : 多态作业.py
Author  : anne
Time    : 2019-07-31 09:52
Desc:
"""
import pickle

class Base():
    def save(self):
        with open('school.db','wb') as f:
            pickle.dump(self,f)



class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.classes = []
        self.teachers = []
        self.courses = []
    def enroll(self,stu_obj):
        print('为学员 %s 办理注册' %self.stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,stu_obj):
        print('雇佣新员工 %s' %self.staff_obj.name)




class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass
class Classes(object):
    def __init__(self,name,account):
        self.name = name
        #人数
        self.account = account



class Teachers(SchoolMember):
    def __init__(self,name,age,sex,salary):
        super(Teachers,self).__init__(self,name,age,sex)
        self.salary = salary


class Courses():
    def __init__(self,name,date,price,school):
        self.name = name
        #开课时间
        self.date = date
        #学费
        self.price = price
        self.school = school

class Students():
    pass