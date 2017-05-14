#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/14 21:14
# @Author  : Mpetrel
# @Site    : 
# @File    : mzt.py
# @Software: PyCharm Community Edition
from flask import Blueprint, request, jsonify
from db import data

mzt = Blueprint('mzt', __name__)

@mzt.route('/list/<int:page>', methods=['GET','POST'])
def imgs_list(page):
    now_page = page * 10
    sql = "select id, title, logo from tm_pic_info limit ?, 10"
    result = data.query(sql, (now_page, ))
    return jsonify(result)


@mzt.route('/detail/<id>', methods=['GET','POST'])
def imgs_detail(id):
    if(not id):
        result = []
    else:
        sql = "select url from tm_pic_detail where info_id = ?"
        database_result = data.query(sql, (id,))
        result = []
        for url in database_result:
            result.append(url[0])

    return jsonify(result)