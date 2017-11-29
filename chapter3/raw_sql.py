#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from settings import MYSQL_URI

engine = create_engine(MYSQL_URI)

with engine.connect() as con:
    con.execute('DROP TABLE IF EXISTS users')

    con.execute('CREATE TABLE users(Id INT PRIMARY KEY AUTO_INCREMENT,'
                'Name VARCHAR(25))')

    con.execute('INSERT INTO users(name) value("xiaoming")')
    con.execute('INSERT INTO users(name) value("xiaowang")')

    rs = con.execute('SELECT * FROM users')

    for row in rs:
        print row
