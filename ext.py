#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    存放扩展的封装
"""
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'signin'


@login_manager.user_loader
def load_user(userid):
    print userid
    try:
        #: Flask Peewee used here to return the user object
        return DPUser.get_id(userid)
    except DPUser.DoesNotExist:
        return None


db = SQLAlchemy()


from account_app.models import DPUser
