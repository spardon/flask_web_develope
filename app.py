#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template
from home_app.base import base_site
from account_app.account import profile

app = Flask(__name__)


# 注册模块
app.register_blueprint(base_site)
app.register_blueprint(profile)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
