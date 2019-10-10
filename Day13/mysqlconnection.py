#!/usr/bin/env python
# coding:utf-8
"""
Name : mysqlconnection.py
Author  : anne
Time    : 2019-09-04 13:31
Desc:
"""
import pymysql

#创建链接
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='',db='anne')
#创建游标
cursor = conn.cursor()
#执行sql,并返回受影响的行数
effect_row = cursor.execute('select * from student')
#返回表中第一条内容
print(cursor.fetchone())
print('--------------------')
#返回表中所有的数据
print(cursor.fetchall())
data = [('N1',22,'2019-09-08','M'),
        ('N2',12,'2019-09-10','F'),
        ('N3',43,'2019-08-23','M')
    ]
cursor.executemany('insert into student (name,age,register_date,sex) values (%s,%s,%s,%s)',data)
#提交
conn.commit()