#!/usr/bin/env python
# coding:utf-8
"""
Name : configparser读取.py
Author  : anne
Time    : 2019-07-28 18:09
Desc:
"""
import configparser
config = configparser.ConfigParser()
config.read('example.ini')
print(config.defaults())
#读取某字段
print(config['bitbucket.org']['user'])

#删除某字段、
sec = config.remove_section('bitbucket.org')
config.write(open('example.cfg','w'))