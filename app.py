#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/05/05 16:32
# @Author  : Mpetrel
# @Site    : 
# @File    : app.py
# @Software: PyCharm Community Edition
from flask import Flask
from route.mzt import mzt
from route.my_response import MyResponse

app = Flask(__name__)
app.response_class = MyResponse
app.register_blueprint(mzt, url_prefix='/mzt/v1')

@app.route("/")
def index():
    return "hello world!"

if __name__ == '__main__':
    app.run(port=8080, debug=True)