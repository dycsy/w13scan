#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 9:57 PM
# @Author  : w8ay
# @File    : config.py

REPOSITORY = "https://github.com/boy-hack/w13scan.git"
VERSION = '0.1'

SERVER_ADDR = ('127.0.0.1', 7778)
THREAD_NUM = 10  # 线程数量

EXCLUDES = [".*\.google", ".*\.lastpass", 'baidu\.com']  # 扫描排除网址(正则表达式)
INCLUDES = [".*"]  # 扫描允许网址(正则表达式)

EXCLUDE_PLUGINS = []  # 不使用的插件，文件名
INCLUDE_PLUGINS = ['all']  # 使用插件,文件名，all为全部

RETRY = 2  # 超时重试次数
TIMEOUT = 10  # 超时时间

LEVEL = 0  # 根据检测深度由浅入深分为1～5级别，级别越高使用插件越多。

if LEVEL >= 1:
    # 等级为1，只使用简单对网站无影响的插件
    INCLUDE_PLUGINS = ['jsonp.py', 'cors.py', 'php_real_path.py', 'errorpage.py', 'directory_browse.py',
                       'js_sensitive_content.py', 'analyze_parameter.py']
if LEVEL >= 2:
    INCLUDE_PLUGINS.extend(
        ['sql_inject_error', 'sql_inject_time', 'directory_browse.py', 'repository_leak.py', 'errorpage.py'])

# DEBUG
# INCLUDE_PLUGINS = ['php_real_path.py', 'js_sensitive_content.py']
# THREAD_NUM = 1
