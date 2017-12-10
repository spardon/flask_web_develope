#!/usr/bin/env python
# -*- coding:utf-8 -*-
import _env
from app import db, create_app


class DPUser(db.Model):
    """
        用户信息表
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)


if __name__ == '__main__':
    db.create_all(app=create_app())
