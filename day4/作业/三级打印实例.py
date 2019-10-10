#!/usr/bin/env python
# coding:utf-8
"""
Name : 三级打印实例.py
Author  : anne
Time    : 2019-07-26 17:27
Desc:
"""
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}


exit_flag = True
while not exit_flag:
    for i in menu:
        print(i)
    choice = input('选择进入1>>')
    if choice in menu:
        while not exit_flag:
            for i2 in menu[choice]:
                print('\t',i2)
    choice2 = input('选择进入2>>')
    if choice2 in menu[choice]:
        while not exit_flag:
            for i3 in menu[choice][choice2]:
                print('\t\t',i3)
    choice3 = input('选择进入3>>:')
    if choice3 in menu[choice][choice2]:
        for i4 in menu[choice][choice2][choice3]:
            print('\t\t',i4)
        choice4 = input('最后一层，按b返回>>:')
        if choice4 == 'b':
            pass
        elif choice4 == 'q':
            exit_flag = True


