#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from flask import session
from app.auth import auth
from app import cache
from app.auth.auth_db import auth_db
from app.config_params.functions import validate_user, validate_params
from app.common.functions import api_response, md5
from app.common.config_error import *

@auth.route('/index', methods=['GET', 'POST'])
def index():
    return 'Hello world!'

@auth.route('/login', methods=['POST'])
@validate_params
def login(params):
    # 用户登录

    params['name'] = params['input']['name']
    params['password'] = params['input']['password']

    user_info = auth_db.query_user_by_name(params['name'], timeout=0)

    # 检查用户信息
    if not user_info:
        return api_response({'c': EC_LOGIN_USER_NOT_EXIST, 'msg': 'user_not_exist'})

    if user_info['password'] != md5(params['password']):
        return api_response({'c': EC_LOGIN_USER_ACCOUNT_ERROR, 'msg': 'password_error'})

    # 写session
    session['name'] = user_info['name']

    return api_response({'c': 0})

@auth.route('/insert', methods=['POST'])
@validate_user
def insert(params):
    # 用户登录

    # 格式化参数
    params['name'] = params['input']['name']

    # 检查用户信息
    user_info = auth_db.query_user_by_name(params['name'])
    if user_info:
        return api_response({'c': EC_LOGIN_USER_ACCOUNT_ERROR, 'msg': 'user_exist'})

    # 格式参数
    params['password'] = md5(params['password'])

    # 插入用户信息
    auth_db.insert_user(params)

    return api_response({'c': 0})

@auth.route('/cache')
@cache.cached(timeout=5, key_prefix='cached_test')
def root():
    t = time.time()
    return str(t)
