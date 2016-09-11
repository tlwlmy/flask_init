#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from app import db

class Base(db.Model):
    # models底层抽象类
    __abstract__ = True

    def save(self):
        # 执行数据库插入

        db.session.add(self)
        db.session.commit()

    def update(self):
        # 执行数据库更新

        db.session.commit()

    def _asdict(self):
        # 获取参数字典

        final = self.__dict__
        if '_sa_instance_state' in final.keys():
            del final['_sa_instance_state']
        return final
