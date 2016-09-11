#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.05.01 tlwlmy
#
from app import create_app
from app.common.functions import api_response
from flask import url_for

app = create_app()

@app.route('/page')
def indexPage():
    return 'Index Page'

# 上线文测试
with app.test_request_context():
    print 'new'
    print url_for('index')
    print url_for('indexPage')
