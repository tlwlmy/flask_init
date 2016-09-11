#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016.05.04 tlwlmy
#

from config import CELERY_BROKER_URL
from celery import Celery

class TaskCelery():
    __celery = None

    def __init__(self):
        # 初始化Celery
        self.__celery = Celery(broker=CELERY_BROKER_URL)

    def __del__(self):
        # 关掉Celery链接
        self.__celery.close()

    def send_wechat_card(self, wechat_card, queue='sendCard') :
        # 发送用户专属名片
        self.__celery.send_task('apps.send_2wx.send_card.send_qrcode', (wechat_card,), queue=queue, compression='zlib', serializer='json')

# 实例
task_celery = TaskCelery()
