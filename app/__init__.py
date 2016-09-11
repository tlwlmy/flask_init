#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.05.01 tlwlmy
#
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.redis import FlaskRedis
from flask.ext.cache import Cache
from config import config, run_env
from flask.ext.session import Session
db = SQLAlchemy()
redis_store = FlaskRedis()
cache = Cache()
sess = Session()

def create_app(config_name=None):
    app = Flask(__name__)
    if not config_name:
        config_name = run_env
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    redis_store.init_app(app)
    cache.init_app(app, config=config[config_name].FLASK_CACHE_CONFIG)
    sess.init_app(app)

    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler(app.config['LOG_PATH'],
                                       maxBytes=1024*1024, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    # 微信接口
    from .wechat import wechat as wechat_blueprint
    app.register_blueprint(wechat_blueprint, url_prefix='/wechat')

    # 公众号
    from .application import application as application_blueprint
    app.register_blueprint(application_blueprint, url_prefix='/app')

    # 用户
    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')

    # 数据
    from .stat import stat as stat_blueprint
    app.register_blueprint(stat_blueprint, url_prefix='/stat')

    # 授权
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # HTTP CODE
    from .error import error as error_blueprint
    app.register_blueprint(error_blueprint, url_prefix='/error')

    return app
