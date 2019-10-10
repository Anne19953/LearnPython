#!/usr/bin/env python
# coding:utf-8
"""
Name : configparser生成模块.py
Author  : anne
Time    : 2019-07-28 18:00
Desc:
"""

import configparser
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval':45,'Compression':'yes',
                     'CompressionLevel':'9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'
topsecret['ForwardX11'] = 'no'
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini','w') as configfile:
    config.write(configfile)