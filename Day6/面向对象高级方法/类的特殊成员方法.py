#!/usr/bin/env python
# coding:utf-8
"""
Name : 类的特殊成员方法.py
Author  : anne
Time    : 2019-07-31 17:00
Desc:
"""

# __doc__　　表示类的描述信息
class Foo:
    """
    试一下__doc__方法
    """
    def func(self):
        pass

print(Foo.__doc__)

##################################
#__module__ 表示当前操作的对象在那个模块
#__class__     表示当前操作的对象的类是什么

from lib.aa import C

obj = C()
print(obj.__module__)  #当前对象所在的模块
print(obj.__class__)  #当前对象所在的类

#####################################
"""构造方法的执行是由创建对象触发的，即：对象 = 类名() ；
而对于 __call__ 方法的执行是由对象后加括号触发的，即：对象() 或者 类()()"""
class Foo:
    def __init__(self):
        pass
    def __call__(self,*args,**kwargs):
        print('__call__')

obj = Foo()
obj()   #等价于 Foo()()

#######################################
#__dict__ 查看类或对象中的所有成员 　　

class Province:
    country = 'China'
    def __init__(self,name,count):
        self.name = name
        self.count = count
    def func(self,*args,**kwargs):
        print('func')

#获取类的成员，即：静态字段，方法
infos = Province.__dict__
# for key,value in infos.items():
#     print('%s : %s'%(key,value))
# print(dict(Province.__dict__))

obj1 = Province('Anne',25000)
print(obj1.__dict__)
#获取 对象obj1 的成员
#输出 {'name': 'Anne', 'count': 25000}


####################################
#一个类中定义了__str__方法，那么在打印 对象 时，默认输出该方法的返回值
class Foo:
    def __str__(self):
        return 'Anne'
obj = Foo()
print(obj)
#输出 Anne

####################################
#__getitem__、__setitem__、__delitem__
#用于索引操作，如字典。以上分别表示获取、设置、删除数据
class Foo(object):
    def __getitem__(self, key):
        print('__getitem__',key)

    def __setitem__(self,key,value):
        print('__setitem__',key,value)

    def __delitem__(self,key):
        print('__delitem__',key)

obj = Foo()
result = obj['k1']    #自动触发执行 __getitem__
obj['k2'] = 'anne'     #自动触发执行  __setitem__
del obj['k1']

###############################################
#
# class Foo(object):
#      def __init__(self,name):
#         self.name = name
#
#
# f = Foo('anne')
# print(type(f))
# print(type(Foo))

def func(self):
    print('hello %s'%self.name)

def __init__(self,name,age):
    self.name = name
    self.age = age

Foo = type('Foo',(),{'func':func,'__init__':__init__})
f = Foo('anne',23)
f.func()
# print(type(Foo))


