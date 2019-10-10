#!/usr/bin/env python
# coding:utf-8
"""
Name : 高阶函数复习作业.py
Author  : anne
Time    : 2019-08-01 11:17
Desc:
"""

"""
1.  利用map()函数，把用户输入的不规范的英文名字，
    变为首字母大写，其他小写的规范名字。
    输入：['adam', 'LISA', 'barT']，
    输出：['Adam', 'Lisa', 'Bart']
"""
# def normalize(m):
#     return m.title()
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize,L1))
# print(L2)

"""
    2.Python提供的sum()函数可以接受一个list并求和，
    请编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
from functools import reduce

# res = reduce(lambda a,b:a*b,[3, 5, 7, 9])
# print(res)  #法1


# def pro(x,y):
#     return x*y
# def prod(L):
#     return(reduce(pro,L))
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('测试成功!')
# else:
#     print('测试失败!')


"""
   3. 利用map和reduce编写一个str2float函数，
    把字符串'123.456'转换成浮点数123.456
"""
# from functools import reduce
# def str2float(s):
#     m,n = s.split('.')
#     def dra(st):
#         return int(st)
#     return reduce(lambda x,y:x*10+y,map(dra,m))+reduce(lambda x,y:x*0.1+y,map(dra,n[::-1]))*0.1




# print('str2float(\'123.456\') =', str2float('123.456'))
# if abs(str2float('123.456') - 123.456) < 0.00001:
#     print('测试成功!')
# else:
#     print('测试失败!')
#
# print(str2float('456.789'))

"""
4.用filter求素数

"""
#奇数序列
# def _odd_iter():
#     n = 1
#     while True:
#         n = n+2
#         yield n

#筛选函数
# def _not_divisible(n):
#     return lambda x:x % n > 0


#生成器，不断返回下一个素数
# def primes():
#      yield 2
#      it = _odd_iter()
#      while True:
#          n = next(it)
#          yield n
#          it = filter(_not_divisible(n),it)
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break



"""
回数是指从左向右读和从右向左读都是一样的数，
例如12321，909。请利用filter()筛选出回数
"""
# def is_palindorm(n):
#     return str(n) == str(n)[::-1]
# output = filter(is_palindorm,range(1,1001))
# print('1-1000:',list(output))
#
# print(is_palindorm(12321))
#
# n = 123
# print(str(n),str(n)[::-1])


"""
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
请用sorted()对上述列表分别按名字排序：

再按成绩从高到低排序：
"""
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L1 = sorted(L,key=by_name)
print(L1)

def by_grade(t):
    return t[1]
L2 = sorted(L,key=by_grade)
print(L2)