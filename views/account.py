#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, Blueprint, request


profile = Blueprint('account', __name__, url_prefix='/account', template_folder='templates')


@profile.route('/login/', methods=['GET', 'POST'])
def login():
    """
        登陆页面
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