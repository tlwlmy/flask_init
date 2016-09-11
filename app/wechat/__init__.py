#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim:fenc=utf-8
# @author tlwlmy
# @version 2016-09-11

from flask import Blueprint

wechat = Blueprint('wechat', __name__)

from . import views
