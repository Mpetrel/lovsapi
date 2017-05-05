#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/05/05 16:32
# @Author  : Mpetrel
# @Site    : 
# @File    : app.py
# @Software: PyCharm Community Edition
import db.data as mdb

if __name__ == "__main__":
    mdb.insert('select * from stocks')
