#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/05/05 17:02
# @Author  : Mpetrel
# @Site    : 
# @File    : data.py
# @Software: PyCharm Community Edition

import sqlite3

db_location = 'data.db'


def insert(sql):
    con = sqlite3.connect(db_location)
    cursor = con.cursor()
    cursor.execute(sql)
    cursor.close()
    con.close()
    pass
