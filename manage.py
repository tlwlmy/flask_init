#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from app import create_app
from app.common.functions import api_response
from flask.ext.script import Manager
from flask import url_for

app = create_app()
manager = Manager(app)


from app import redis_store

# 全局函数
@app.template_global('record_name')
def record_name(name):
    # 检查是否访问过
    result = redis_store.get(name)
    if result is not None:
        return True
    redis_store.set(name, 1, 86400)
    return False

# 过滤器
@app.template_filter('sub')
def sub(l, start, end):
    return l[start:end]

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    # app.run()
    manager.run()

@app.route('/page')
def indexPage():
    return 'Index Page'

with app.test_request_context():
    print url_for('indexPage')
