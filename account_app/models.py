#!/usr/bin/env python
# -*- coding:utf-8 -*-
import _env
from flask_login import UserMixin
from datetime import datetime
from ext import db


class DPUser(db.Model):
    """
        用户信息表
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False, index=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username



