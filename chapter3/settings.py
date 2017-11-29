#!/usr/bin/env python
# -*- coding:utf-8 -*-

DEBUG = True

class MYSQLDB(object):
    HOSTNAME = 'localhost'
    DATABASE = 'r'
    USERNAME = 'web'
    PASSWORD = 'web'

MYSQL_URI = 'mysql://{}:{}@{}/{}'.format(
    MYSQLDB.USERNAME, MYSQLDB.PASSWORD,
    MYSQLDB.HOSTNAME, MYSQLDB.DATABASE
)
