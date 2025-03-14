#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
FilePath: /PyWebView/vue-pywebview-pyinstaller/pyapp/mainCEF.py
Author: 潘高
LastEditors: 潘高
Date: 2022-03-23 15:41:46
LastEditTime: 2022-03-23 15:45:04
Description: 生成客户端主程序【CEF模式】
usage: 运行前，请确保本机已经搭建Python3开发环境，且已经安装 pywebview 模块。
'''

import os
import sys

import webview

# @fix https://blog.csdn.net/qq_40472613/article/details/119670598
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)

from api.api import API
from config.config import Config

# 前端页面目录
if sys.flags.dev_mode:
    MAIN_DIR = os.path.join("..", "dist")  # 开发环境
    DEBUG = True
else:
    MAIN_DIR = os.path.join(".", "web")  # 生产环境
    DEBUG = False


def WebViewApp():
    api = API()    # 本地接口
    cfg = Config()    # 配置文件

    template = os.path.join(MAIN_DIR, "index.html")    # 设置页面，可以指向远程或本地
    if sys.flags.dev_mode:
        template = 'http://localhost:3000/index.html'

    window = webview.create_window(title=cfg.appName, url=template, js_api=api, confirm_close=True, min_size=(
        800, 400), text_select=True)    # 创建窗口
    api.window = window

    webview.start(localization={
        'cocoa.menu.quit': u'确定退出应用吗?',
    }, debug=DEBUG, http_server=True, gui='cef')    # 启动窗口


if __name__ == "__main__":
    WebViewApp()
