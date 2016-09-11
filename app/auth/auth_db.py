#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from app import redis_store
from app.common.decorator import cached
from app.common.constant import Duration
from models import User

class AuthDb(object):
    # 授权查询

    @cached(timeout=Duration.HalfHour)
    def query_user_by_name(self, name):
        # 根据用户姓名查询用户信息

        record = User.query.filter(User.name==name).first()

        # 格式参数
        final = record._asdict() if record else {}

        return final

    def insert_user(self, modify_info):
        # 插入用户信息

        white_fields = [
            'name', 'password'
        ]

        final = {field: modify_info[field] for field in white_fields if field in modify_info.keys()}

        # 插入数据库
        record = User(**final)
        record.save()

        # 更新uid查询缓存
        cache_key = "query_user_by_name:{0}".format(record.name)
        redis_store.delete(cache_key)

        final = record._asdict()

        return final


# 实例
auth_db = AuthDb()
