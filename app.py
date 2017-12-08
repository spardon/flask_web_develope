#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template

from ext import db

from home_app.base import base_site
from account_app.account import profile

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)


# 注册模块
app.register_blueprint(base_site)
app.register_blueprint(profile)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
