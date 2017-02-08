#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from flask import session, render_template
from app.auth import auth
from app import cache
from app.auth.auth_db import auth_db
from app.validate.functions import validate_admin_user, validate_params
from app.common.functions import api_response, md5, generate_str
from app.common.config_error import *

@auth.route('/index', methods=['GET', 'POST'])
def index():
    return 'Hello world!'

@auth.route('/login', methods=['POST'])
@validate_params
def login(params):
    # 用户登录

    # 格式化参数
    params['name'] = params['input']['name']
    params['password'] = params['input']['password']

    params['user_info'] = auth_db.query_user_by_name(params['name'], timeout=0)

    # 检查用户信息
    if not params['user_info']:
        return api_response({'c': EC_LOGIN_USER_NOT_EXIST, 'msg': 'user_not_exist'})

    if params['user_info']['password'] != md5(params['password']):
        return api_response({'c': EC_LOGIN_USER_ACCOUNT_ERROR, 'msg': 'password_error'})

    # 写session
    session['name'] = params['user_info']['name']

    return api_response({'c': 0})

@auth.route('/insert', methods=['POST'])
@validate_admin_user
def insert(params):
    # 用户登录

    # 格式化参数
    params['name'] = params['input']['name']
    params['password'] = params['input']['password']

    # 检查用户信息
    params['user_info'] = auth_db.query_user_by_name(params['name'])
    if params['user_info']:
        return api_response({'c': EC_LOGIN_USER_ACCOUNT_ERROR, 'msg': 'user_exist'})

    # 格式参数
    params['password'] = md5(params['password'])

    # 插入用户信息
    auth_db.insert_user(params)

    return api_response({'c': 0})

@auth.route('/update', methods=['POST'])
@validate_admin_user
def update(params):
    # 用户登录

    # 格式化参数
    params['name'] = params['input']['name']
    params['password'] = params['input']['password']

    # 检查用户信息
    params['user_info'] = auth_db.query_user_by_name(params['name'])
    if not params['user_info']:
        return api_response({'c': EC_RECORD_NOT_EXIST, 'msg': 'record_not_exist'})

    # 格式参数
    params['password'] = md5(params['password'])

    # 更新用户信息
    auth_db.update_user(params['user_info'], {'password': params['password']})

    return api_response({'c': 0})

@auth.route('/cache')
@cache.cached(timeout=5, key_prefix='cached_test')
def root():
    t = time.time()
    return str(t)

@auth.route('/admin')
def admin():
    # 后台框架页面
    return render_template('index.html')

@auth.route('/mulit_deal')
def mulit_deal():
    # 批量处理
    record = [
        {'uid': 10, 'name': 4, 'b': 0, 'password': 4},
        {'uid': 11, 'name': 5, 'b': 0, 'password': 5},
        {'uid': 9, 'name': 3, 'b': 0, 'password': 4},
        {'uid': 8, 'name': 2, 'b': 0, 'password': 5},
    ]

    modify_info = [
        {'name': 4, 'b': 0, 'password': 10},
        {'name': 5, 'b': 0, 'password': 11},
    ]
    from app.common.functions import compare_lists

    record_lists, update_lists, insert_lists, delete_lists = compare_lists(record, modify_info, ['name'])

    # 批量更新
    auth_db.update_multi_user(record_lists, update_lists)

    # 批量插入
    auth_db.insert_multi_user(insert_lists)

    # 批量删除
    auth_db.delete_mutli_user(delete_lists)

    return api_response({'c': 0})
