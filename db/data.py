#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/05/05 17:02
# @Author  : Mpetrel
# @Site    : 
# @File    : data.py
# @Software: PyCharm Community Edition

import sqlite3

db_location = 'data.db'


def connect_database():
    con = sqlite3.connect(db_location)
    cursor = con.cursor()
    return con, cursor

def query(sql, param):
    con, cursor = connect_database()
    data = cursor.execute(sql, param)
    results = data.fetchall()
    cursor.close()
    con.close()
    return results

