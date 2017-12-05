#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint, render_template, abort

base_site = Blueprint('base', __name__, template_folder='templates')


@base_site.route('/index')
def index():
    return render_template('index.html')
