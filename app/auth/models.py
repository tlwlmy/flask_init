#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from app import db
from datetime import datetime
from app.common.base import Base, insert_filter, update_filter

class User(Base):
    # __bind_key__ = 'wechat'   # 数据库路由
    __tablename__= 'user'
    uid = db.Column(db.Integer, primary_key=True)  # 用户id
    name = db.Column(db.String(64), unique=True, index=True)  # 用户名
    password = db.Column(db.String(32), index=True)  # 用户密码
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    last_edit = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 最后编辑时间

    # 插入数据库列表
    _insert_fields = ['name', 'password']

    # 更新数据库字段列表
    _update_fields = ['password']

    @staticmethod
    @insert_filter(_insert_fields)
    def insert(modify_info):
        # 插入
        record = User(**modify_info)

        return record

    @staticmethod
    @update_filter(_update_fields)
    def update(record, modify_info):
        # 更新
        affected_row = User.query.filter(User.uid==record['uid']).update(modify_info)

        return affected_row, modify_info
