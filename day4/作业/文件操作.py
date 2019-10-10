#!/usr/bin/env python
# coding:utf-8
"""
Name : 文件操作.py
Author  : anne
Time    : 2019-07-26 20:07
Desc:
"""
#读文件
# data = open('yesterday',encoding = 'utf-8').read()
# f = open('yesterday','r',encoding='utf-8')
# data = f.read()
# print(data)

#写文件
# f = open('today','w',encoding='utf-8')
# data = f.write('我也好想去实习呀\n又想挣钱了\n')

#前读5行
# f = open('yesterday','r',encoding='utf-8')
# for i in range(5):
#     print(f.readline())

#第十行不打印

''' 不推荐使用
f = open('yesterday','r',encoding='utf-8')
for index,line in enumerate(f.readlines()):
    if index == 9:
        print('--------我是分割线-------')
        continue
    print(line.strip())
'''



#推荐使用  迭代器
# f = open('yesterday','r',encoding='utf-8')
# count = 0
# for line in f:
#     if count == 9:
#         print('--------我是分割线------')
#         count += 1
#         continue
#     print(line)
#     count += 1


#tell()按字符计数，光标位置
# f = open('yesterday','r',encoding='utf-8')
# print(f.readline())
# print(f.tell())
#seek()回到某位置
# f.seek(0)
# print(f.readline())

#当前编码
# print(f.encoding)


#截断
# f = open('yesterday2','a',encoding='utf-8')
# f.truncate(20)

#修改
f = open('yesterday2','r',encoding='utf-8')
f_new = open('yesterday2.bak','w',encoding='utf-8')

for line in f:
    if '肆意的快乐等我享受' in line:
        line = line.replace('肆意的快乐等我享受','肆意的快乐等Anne享受')
    f_new.write(line)

f.close()
f_new.close()


