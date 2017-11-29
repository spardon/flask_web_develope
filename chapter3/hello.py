#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)

app.config.from_object('settings')


@app.route('/')
def hello_word():
    return 'Hello World!'


@app.route('/item/<id>')
def item(id):
    return 'Item:{}'.format(id)


if __name__  == '__main__':
    app.run(host='0.0.0.0', port=9000)
