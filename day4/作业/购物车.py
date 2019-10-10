#!/usr/bin/env python
# coding:utf-8
"""
Name : 购物车.py
Author  : ane
Time    : 2019-07-26 16:36
Desc:
"""
import os
product_list = [
    ['Iphone7',5800],
    ['Mac Pro',9800],
    ['Bike',800],
    ['Watch',10600],
    ['Coffee',31],
    ['Alex Python',120]
]

shopping_list = []
salary = input('Input your salary:')
if salary.isdigit():
    salary = int(salary)
    while True:
        # for item in product_list:
        #     print(product_list.index(item),item)  #将下标索引也打印出来
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input('>>>>>>>选择要买的物品:')
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >=0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary: #买得起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print('Added  %s into shopping cart,your current balance is \033[31;1m%s\033[0m '%(p_item,salary))
                else:
                    print('\033[41;1m你的余额还剩[%s],不够了\033[0m' %salary)
            else:
                print('商品不存在，请重新输入！')

        elif user_choice == 'q':
            print('-----------shopping list-----------')
            for p in shopping_list:
                print(p)
            print('your current balance is [%s]'%salary)
            exit()
        else:
            print('invalid option')

