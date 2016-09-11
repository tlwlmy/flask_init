#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.06 tlwlmy
#

import pickle
from uuid import uuid4
from werkzeug.datastructures import CallbackDict
from app import redis_store

class RedisSession(CallbackDict):

    def __init__(self, initial=None, sid=None):
        # CallbackDict.__init__(self, initial, on_update)
        super(RedisSession, self).__init__(initial)
        self.sid = sid


class RedisSessionInterface(object):
    serializer = pickle
    session_class = RedisSession

    def __init__(self, prefix='session:', session_cookie_name='session_id', session_lifetime=86400, user_prefix='muid_session:'):
        self.prefix = prefix
        self.session_cookie_name = session_cookie_name
        self.session_lifetime = session_lifetime
        self.user_prefix = user_prefix

    def generate_sid(self):
        return str(uuid4())

    def save_user_session(self, session):
        # 保存用户session记录
        if 'muid' in session.keys():
            cache_key = self.user_prefix + str(session['muid'])
            sid = redis_store.get(cache_key)
            if sid is not None and sid != session.sid:
                self.del_session(sid)
            redis_store.setex(cache_key, session.sid, self.session_lifetime)

    def del_session(self, sid):
        # 删除session
        redis_store.delete(self.prefix + sid)

    def open_session(self, sid=None):
        # 获取session
        if sid is None:
            sid = self.generate_sid()
            return self.session_class(sid=sid)
        val = redis_store.get(self.prefix + sid)
        if val is not None:
            data = self.serializer.loads(val)
            return self.session_class(data, sid=sid)
        return self.session_class(sid=sid)

    def save_session(self, session):
        # 保存session
        val = self.serializer.dumps(dict(session))
        redis_store.setex(self.prefix + session.sid, val, self.session_lifetime)
        self.save_user_session(session)

    def modify_session(self, sid, modify):
        # 更新session信息
        session = self.open_session(sid)

        session = dict(session, **modify)

        self.save_session(session)
