#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 22:20
# @Author  : Mpetrel
# @Site    : 
# @File    : my_response.py
# @Software: PyCharm Community Edition
# 源码来自：http://zengrong.net/post/2615.htm

from werkzeug.datastructures import Headers
from werkzeug.wrappers import Response


class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
        else:
            headers = Headers([origin, methods])
        kwargs['headers'] = headers
        super(MyResponse, self).__init__(response, **kwargs)
