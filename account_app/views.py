#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
    账户相关视图
"""
from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask_login import login_user

profile = Blueprint('account', __name__, template_folder='templates')


@profile.route('/signin/', methods=['GET', 'POST'])
def signin():
    """
        登录界面
    """
    context = {'title': u'登录'}
    if request.method == 'GET':
        return render_template('profile/login.html', **context)

    username = request.form['username']
    password = request.form['password']
    user = DPUser.query.filter_by(username=username, password=password).first()
    if user is None:
        flash('用户名或密码错误', 'error')

        print "============="
        return redirect(url_for('account.signin'))
    login_user(user)
    flash('登录成功！', 'success')
    return redirect(url_for('base.index'))


@profile.route('/signup/', methods=['GET', 'POST'])
def signup():
    """
    注册界面
    :return: 注册模板或跳转首页
    """
    context = {'title': u'注册'}
    if request.method == 'GET':
        return render_template('profile/register.html', **context)

    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    user = DPUser(username, email, password)
    db.session.add(user)
    db.session.commit()
    flash('注册成功！')
    return redirect(url_for('account.signin'))


from app import db, login_manager
from models import DPUser
