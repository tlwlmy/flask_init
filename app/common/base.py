#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from app import db
from functools import wraps
from app.common.functions import filter_fields, compare_fields

class Base(db.Model):
    # models底层抽象类
    __abstract__ = True

    def save(self):
        # 执行数据库插入

        db.session.add(self)
        db.session.commit()

    def commit(self):
        # 执行数据库更新

        db.session.commit()

    def _asdict(self):
        # 获取参数字典

        final = self.__dict__
        if '_sa_instance_state' in final.keys():
            del final['_sa_instance_state']
        return final

def insert_filter(white_fields=[]):
    # 插入参数过滤装饰器
    def wrapper_fun(func):
        @wraps(func)
        def _wrapper_fun(*args, **kwargs):

            # 过滤参数
            kwargs['modify_info'] = filter_fields(white_fields, kwargs['modify_info'])

            # 调用插入方法
            record = func(*args, **kwargs)
            record.save()

            return record
        return _wrapper_fun
    return wrapper_fun

def insert_multi_filter(white_fields=[]):
    # 插入参数过滤装饰器
    def wrapper_fun(func):
        @wraps(func)
        def _wrapper_fun(*args, **kwargs):
            # 过滤参数
            for index in range(0, len(kwargs['modify_info'])):
                kwargs['modify_info'][index] = filter_fields(white_fields, kwargs['modify_info'][index])

            # 调用插入方法
            record = func(*args, **kwargs)

            # 批量保存
            db.session.add_all(record)
            db.session.commit()

            return record
        return _wrapper_fun
    return wrapper_fun

def update_filter(white_fields=[]):
    # 更新参数过滤装饰器
    def wrapper_fun(func):
        @wraps(func)
        def _wrapper_fun(*args, **kwargs):

            # 过滤参数
            kwargs['modify_info'] = compare_fields(white_fields, kwargs['record'], kwargs['modify_info'])
            if kwargs['modify_info']:
                # 更新
                affected_row = func(*args, **kwargs)
                db.session.commit()

                return affected_row, kwargs['modify_info']

            return 0, {}

        return _wrapper_fun
    return wrapper_fun

def update_multi_filter(white_fields=[]):
    # 更新参数过滤装饰器
    def wrapper_fun(func):
        @wraps(func)
        def _wrapper_fun(*args, **kwargs):
            # 过滤参数
            print kwargs
            for key in kwargs['modify_info'].keys():
                if key in kwargs['record'].keys():
                    kwargs['modify_info'][key] = compare_fields(white_fields, kwargs['record'][key], kwargs['modify_info'][key])

            if kwargs['modify_info']:
                # 更新
                affected_row = func(*args, **kwargs)
                db.session.commit()

                return affected_row, kwargs['modify_info']

            return [], {}

        return _wrapper_fun
    return wrapper_fun
