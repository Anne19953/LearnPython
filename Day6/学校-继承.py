#!/usr/bin/env python
# coding:utf-8
"""
Name : 学校-继承.py
Author  : anne
Time    : 2019-07-30 20:04
Desc:
"""


class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.staffs = []
    def enroll(self,stu_obj):
        print('为学员 %s 办理注册手续'%stu_obj.name)
        self.students.append(stu_obj)
    def hire(self,staff_obj):
        print('雇佣新员工 %s ' % staff_obj.name)
        self.staffs.append(staff_obj)


class SchoolMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass



class Teacher(SchoolMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course

    def tell(self):
        print('''---------the info of teacher:
            Name:%s
            Age:%s
            Sex:%s
            Salary:%s
            course:%s
        '''%(self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print('%s is teaching course [%s]'%(self.name,self.course))




class Student(SchoolMember):
    def __init__(self,name,age,sex,stu_id,course):
        super(Student,self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.course = course


    def tell(self):
        print('''---------the info of students:
                Name:%s
                Age:%s
                Sex:%s
                stu_id:%s
                grade:%s
            ''' % (self.name, self.age, self.sex, self.stu_id, self.course))

    def pay_tuition(self,amount):
        print('%s has paid tution for $%s'%(self.name,amount))


t1 = Teacher('yanfei',44,'F',10000,'语文')
t1.tell()
t2 = Teacher('chenlaoshi',40,'F',5000,'数学')
s1 = Student('anne',18,'F,',10001,'语文')
s1.tell()
s2 = Student('songfengju',27,'M','10002','数学')
school = School('北邮','西土城')
school.hire(t1)
school.enroll(s1)
school.enroll(s2)

print(school.students)
print(school.staffs)
school.staffs[0].teach()


for stu in school.students:
    print(stu.pay_tuition(5000))