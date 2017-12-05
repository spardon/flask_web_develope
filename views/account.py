#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import render_template, Blueprint, request


profile = Blueprint('account', __name__, template_folder='templates/profile', url_prefix='account')


@profile.route('/login', methods=['GET', 'POST'])
def login():
    """
        登陆页面
    """
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        pass # 验证账户操作


