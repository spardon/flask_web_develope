#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    账户相关视图
"""
from flask import render_template, Blueprint, request


profile = Blueprint('account', __name__, template_folder='templates')


@profile.route('/signin/', methods=['GET', 'POST'])
def signin():
    """
        注册页面
    """
    if request.method == 'GET':
        return render_template('profile/login.html')

    if request.method == 'POST':
        pass # 验证账户操作


@profile.route('/sign/', methods=['GET','POST'])
def sign():
    """
        注册页面
    """
    if request.method =='GET':
        return render_template('profile/sign.html')