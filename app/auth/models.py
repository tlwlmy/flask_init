#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from app import db
from datetime import datetime
from app.common.base import Base

class User(Base):
    # __bind_key__ = 'wechat'   # 数据库路由
    __tablename__= 'user'
    uid = db.Column(db.Integer, primary_key=True)  # 用户id
    name = db.Column(db.String(64), unique=True, index=True)  # 用户名
    password = db.Column(db.String(32), index=True)  # 用户密码
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    last_edit = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 最后编辑时间
