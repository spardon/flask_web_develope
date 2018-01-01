#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template

from flask_debugtoolbar import DebugToolbarExtension
from home_app.views import base_site
from account_app.views import profile
from ext import login_manager, db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    db.init_app(app)
    login_manager.init_app(app)

    # 注册模块
    app.register_blueprint(base_site)
    app.register_blueprint(profile)

    return app


app = create_app()


toolbar = DebugToolbarExtension(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9011)
